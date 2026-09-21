import os
from typing import TypedDict
from dotenv import load_dotenv

# LangGraph
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

# LangChain e Gemini (CORRIGIDO AQUI)
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

# Ferramentas de Busca
from tavily import TavilyClient
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Interface
import gradio as gr

# 1. CARREGAR VARIÁVEIS DE AMBIENTE (.env)
load_dotenv()
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# Instanciando o Gemini (CORRIGIDO AQUI)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

# 2. DEFININDO O ESTADO (Agent State)
class AgentState(TypedDict):
    task: str
    plan: str
    draft: str
    critic: str
    content: str
    revisions: int

# 3. FUNÇÃO AUXILIAR DE WEB SCRAPING COM SELENIUM
def buscar_com_selenium(query: str) -> str:
    print(f"🕵️ Selenium pesquisando: {query}")
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Roda sem abrir a janela do Chrome
    chrome_options.add_argument("--disable-gpu")
    
    # Inicializa o navegador
    driver = webdriver.Chrome(options=chrome_options)
    try:
        # Usa o DuckDuckGo Lite por ser fácil de extrair dados via scraping
        driver.get("https://lite.duckduckgo.com/lite/")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.submit()
        
        # Coleta os resultados (snippets)
        resultados = driver.find_elements(By.CLASS_NAME, "result-snippet")
        textos = [res.text for res in resultados[:3]] # Pega os 3 primeiros
        return " ".join(textos) if textos else "Nenhum dado extra encontrado."
    except Exception as e:
        return f"Erro no Selenium: {str(e)}"
    finally:
        driver.quit()

# 4. CRIANDO OS NÓS (AGENTES)
def planner_node(state: AgentState):
    print("📝 Planejando a redação...")
    task = state["task"]
    messages = [
        SystemMessage(content="Você é um planejador de artigos. Crie um esboço em tópicos para a tarefa."),
        HumanMessage(content=f"Tarefa: {task}")
    ]
    response = llm.invoke(messages)
    return {"plan": response.content}

def researcher_node(state: AgentState):
    print("🔍 Pesquisando contexto geral (Tavily)...")
    task = state["task"]
    try:
        tavily_resp = tavily_client.search(query=task, search_depth="basic")
        tavily_text = "\n".join([res["content"] for res in tavily_resp["results"]])
    except Exception as e:
        tavily_text = f"Erro no Tavily: {str(e)}"
    
    # Se já houver conteúdo, concatena
    conteudo_atual = state.get("content", "")
    novo_conteudo = conteudo_atual + "\n[Pesquisa Tavily]: " + tavily_text
    return {"content": novo_conteudo}

def generation_node(state: AgentState):
    print(f"✍️ Escrevendo o rascunho (Revisão {state.get('revisions', 0)})...")
    plan = state.get("plan", "")
    content = state.get("content", "")
    messages = [
        SystemMessage(content="Você é um redator especialista. Escreva um artigo de exatos 5 parágrafos usando o plano e os dados fornecidos."),
        HumanMessage(content=f"Plano:\n{plan}\n\nDados de Pesquisa:\n{content}")
    ]
    response = llm.invoke(messages)
    return {"draft": response.content}

def reflection_node(state: AgentState):
    print("🧠 Analisando e criticando o texto...")
    draft = state.get("draft", "")
    messages = [
        SystemMessage(content="Você é um editor rigoroso. Leia o rascunho e identifique se falta alguma informação técnica crucial. Responda APENAS com um termo ou frase curta sobre o que falta pesquisar. Se estiver perfeito, responda 'PERFEITO'."),
        HumanMessage(content=f"Rascunho:\n{draft}")
    ]
    response = llm.invoke(messages)
    return {"critic": response.content}

def critic_research_node(state: AgentState):
    print("🤖 Corrigindo lacunas com Selenium...")
    critic = state.get("critic", "")
    
    if "PERFEITO" not in critic.upper():
        # Usa o Selenium para buscar a informação que o crítico sentiu falta
        novos_dados = buscar_com_selenium(critic)
        conteudo_atual = state.get("content", "")
        conteudo_atualizado = conteudo_atual + f"\n[Dados Adicionais Selenium - {critic}]: " + novos_dados
    else:
        conteudo_atualizado = state.get("content", "")

    revisions = state.get("revisions", 0) + 1
    return {"content": conteudo_atualizado, "revisions": revisions}

# 5. ARESTA CONDICIONAL
def should_continue(state: AgentState):
    critic = state.get("critic", "")
    revisions = state.get("revisions", 0)
    
    # Se o editor aprovou ou chegamos ao limite de iterações, finaliza
    if "PERFEITO" in critic.upper() or revisions >= 2:
        print("✅ Fluxo concluído!")
        return END
    
    print("🔄 Voltando para a geração com novos dados...")
    return "generation"

# 6. MONTANDO O GRAFO
workflow = StateGraph(AgentState)

workflow.add_node("planner", planner_node)
workflow.add_node("researcher", researcher_node)
workflow.add_node("generation", generation_node)
workflow.add_node("reflection", reflection_node)
workflow.add_node("critic_research", critic_research_node)

workflow.set_entry_point("planner")
workflow.add_edge("planner", "researcher")
workflow.add_edge("researcher", "generation")
workflow.add_edge("generation", "reflection")
workflow.add_edge("reflection", "critic_research")
workflow.add_conditional_edges("critic_research", should_continue)

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

# 7. INTERFACE COM GRADIO
def executar_agentes(tarefa):
    config = {"configurable": {"thread_id": "sessao_1"}}
    initial_state = {"task": tarefa, "revisions": 0, "content": ""}
    
    yield "Iniciando os agentes... Olhe o terminal do VS Code para acompanhar os logs!"
    
    final_state = None
    for output in app.stream(initial_state, config=config):
        final_state = output
        # O Gradio vai mostrar a etapa em que o grafo está rodando
        etapa_atual = list(output.keys())[0]
        yield f"Executando agente: {etapa_atual.upper()}..."
        
    # Quando o fluxo termina, ele tenta extrair a chave "draft" da última etapa
    # Como a última etapa pode ser o critic_research, pegamos o estado completo e retornamos o draft
    if final_state:
        ultimo_no = list(final_state.keys())[0]
        rascunho_final = final_state[ultimo_no].get("draft", "Texto finalizado, mas não foi possível exibir o rascunho.")
        # Se a última etapa não retornou o draft (ex: critic_research retorna apenas content/revisions)
        # Vamos tentar pegar do config de estado atual do Langgraph:
        estado_completo = app.get_state(config).values
        yield estado_completo.get("draft", rascunho_final)
    else:
        yield "Erro ao processar o fluxo."

demo = gr.Interface(
    fn=executar_agentes,
    inputs=gr.Textbox(lines=2, placeholder="Ex: Escreva um artigo sobre os impactos da IA na medicina brasileira."),
    outputs=gr.Textbox(label="Rascunho Final", lines=15),
    title="Equipe de Agentes Redatores (Gemini + LangGraph)",
    description="Fluxo: Planejador ➔ Pesquisador (Tavily) ➔ Redator ➔ Crítico ➔ Pesquisador Extra (Selenium)"
)

if __name__ == "__main__":
    demo.launch()