# 🤖 Equipe de Agentes Redatores (IA)

![Exemplo de Uso](1.PNG)

## 📌 O que é este projeto?
Este é um gerador de redações inteligente. Ele usa 5 "agentes" de Inteligência Artificial trabalhando em equipe para planejar, pesquisar na internet, escrever e revisar um artigo completo. Tudo isso usando o **Google Gemini 2.5** e a estrutura do **LangGraph**.

## ⚙️ Como funciona?
1. **Planejador:** Lê o tema que você digitou e cria os tópicos.
2. **Pesquisador:** Busca informações gerais na internet (via Tavily).
3. **Redator:** Escreve o primeiro rascunho do texto.
4. **Crítico:** Lê o rascunho e aponta se faltam dados específicos.
5. **Pesquisador Extra:** Usa um robô (Selenium) para buscar na web exatamente o que o Crítico pediu e manda o redator reescrever.

## 🛠️ Como instalar e rodar

![Exemplo de Uso](1.PNG)

**1. Baixe o projeto e entre na pasta:**
```bash
git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
cd SEU-REPOSITORIO
2. Ative o ambiente e instale as bibliotecas (no Windows):

Bash
python -m venv venv
.\venv\Scripts\activate
pip install python-dotenv langgraph langchain-google-genai selenium tavily-python gradio
3. Configure as Chaves de API:
Crie um arquivo chamado .env na pasta do projeto e coloque suas chaves dentro dele:

Plaintext
GOOGLE_API_KEY="sua_chave_do_gemini_aqui"
TAVILY_API_KEY="sua_chave_do_tavily_aqui"
4. Rode o aplicativo:

Bash
python main.py
O terminal vai gerar um link (ex: http://127.0.0.1:7860). Segure Ctrl e clique nele para abrir a tela no seu navegador e começar a usar!


Para enviar esse novo modelo simples para o seu GitHub, salve o texto acima no seu arquivo `README.md` e rode os comandos de sempre no terminal:

```powershell
git add README.md
git commit -m "Atualiza README para versão simplificada em pt-br"
git push
