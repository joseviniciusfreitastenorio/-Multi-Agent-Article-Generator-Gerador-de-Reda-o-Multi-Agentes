🇺🇸 English
Overview
This project is an advanced multi-agent AI workflow built with LangGraph and powered by Google's Gemini 2.5. It simulates a complete editorial room where 5 specialized agents collaborate, search the web, scrape data, and iterate over drafts to produce a high-quality article.

🚀 Features
Multi-Agent Architecture: Built with LangGraph to manage state and stateful transitions.

Google Gemini 2.5 Integration: Uses the latest Gemini models for planning, writing, and reflection.

Intelligent Web Research: Integrates Tavily API for broad context gathering.

Targeted Web Scraping: Uses Selenium (headless) to fetch specific missing data requested by the Critic Agent.

Interactive UI: Clean, real-time interface built with Gradio, displaying the generation progress.

🧠 The Agents (Workflow)
Planner: Creates an outline based on the user's prompt.

Researcher: Uses Tavily to fetch initial context and data.

Generator: Writes a draft based on the plan and researched data.

Reflection (Critic): Reviews the text strictly to find missing information.

Critic Research: Triggers a Selenium bot to scrape specific answers for the Critic's questions, sending the flow back to the Generator.

🛠️ Configuration & Setup
Clone the repository:

Bash
git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
cd SEU-REPOSITORIO
Create and activate a virtual environment:

Bash
python -m venv venv
# Windows:
.\\venv\\Scripts\\activate
Install dependencies:

Bash
pip install python-dotenv langgraph langchain-google-genai selenium tavily-python gradio
Environment Variables:
Create a .env file in the root directory and add your API keys:

Plaintext
GOOGLE_API_KEY="your_google_gemini_key_here"
TAVILY_API_KEY="your_tavily_key_here"
💻 Usage
Run the application using the following command:

Bash
python main.py
Open the provided local URL in your browser. Type your topic in the "tarefa" box and wait for the agents to process and deliver the final draft.

🇧🇷 Português
Visão Geral
Este projeto é um fluxo de trabalho avançado de Inteligência Artificial multi-agentes construído com LangGraph e alimentado pelo Gemini 2.5 do Google. Ele simula uma redação completa onde 5 agentes especializados colaboram, pesquisam na internet, extraem dados e refinam rascunhos para produzir um artigo de alta qualidade.

🚀 Funcionalidades
Arquitetura Multi-Agentes: Construído com LangGraph para gerenciar o estado e as transições do fluxo.

Integração Google Gemini 2.5: Utiliza os modelos mais recentes do Gemini para planejamento, escrita e reflexão.

Pesquisa Inteligente: Integra a Tavily API para busca de contexto inicial na internet.

Web Scraping Direcionado: Usa Selenium (modo headless) para buscar dados específicos solicitados pelo Agente Crítico.

Interface Interativa: Interface limpa construída com Gradio, que permite acompanhar a execução do fluxo em tempo real.

🧠 Os Agentes (Fluxo de Trabalho)
Planejador (Planner): Cria um esboço em tópicos baseado no tema do usuário.

Pesquisador (Researcher): Usa Tavily para buscar o contexto inicial na web.

Gerador (Generator): Escreve um rascunho usando o plano e os dados pesquisados.

Crítico (Reflection): Revisa o texto rigorosamente em busca de lacunas de informação.

Pesquisador Crítico (Critic Research): Aciona um robô do Selenium para buscar as respostas exigidas pelo Crítico, enviando novos dados de volta para o Gerador.

🛠️ Configuração
Clone o repositório:

Bash
git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
cd SEU-REPOSITORIO
Crie e ative um ambiente virtual:

Bash
python -m venv venv
# Windows:
.\\venv\\Scripts\\activate
Instale as dependências:

Bash
pip install python-dotenv langgraph langchain-google-genai selenium tavily-python gradio
Variáveis de Ambiente:
Crie um arquivo .env na raiz do projeto e adicione suas chaves de API:

Plaintext
GOOGLE_API_KEY="sua_chave_do_google_aqui"
TAVILY_API_KEY="sua_chave_do_tavily_aqui"
💻 Como Usar
Execute a aplicação com o comando:

Bash
python main.py
Abra o link local gerado no seu navegador. Digite o tema desejado na caixa "tarefa" e clique em Submit. Aguarde os agentes trabalharem em background até que o rascunho final seja exibido.
"""

with open("README.md", "w", encoding="utf-8") as f:
f.write(conteudo)

print("✅ Arquivo README.md gerado com sucesso na pasta do projeto!")


3. No terminal do VS Code, execute o script:
```powershell
python gerar_readme.py
Após a mensagem de sucesso, envie a atualização para o GitHub com os três comandos padrão:

PowerShell
git add .
git commit -m "Gera README.md via script e adiciona imagem"
git push
