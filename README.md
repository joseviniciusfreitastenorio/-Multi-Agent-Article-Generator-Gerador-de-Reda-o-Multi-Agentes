

# 🤖 Equipe de Agentes Redatores

 > Um sistema de geração de textos baseado em múltiplos agentes de Inteligência Artificial, utilizando **Google Gemini 2.5**, **LangGraph**, **Tavily**, **Selenium** e **Gradio**.

  <img width="1905" height="954" alt="1" src="https://github.com/user-attachments/assets/e57cd438-fe95-4ece-b0f0-08157348702e" />


 ## 📌 Sobre o projeto

 A **Equipe de Agentes Redatores** é um gerador inteligente de redações que utiliza uma arquitetura de múltiplos agentes de IA para transformar um tema em um texto completo, pesquisado e revisado.

 Em vez de utilizar apenas uma chamada de IA, o projeto divide o processo de produção textual entre **5 agentes especializados**, cada um responsável por uma etapa específica.

 O fluxo combina planejamento, pesquisa na internet, redação, análise crítica e uma segunda etapa de pesquisa para melhorar o resultado final.

---

 ## 🧠 Arquitetura dos agentes

 O sistema é composto por cinco agentes principais:

 | Agente | Responsabilidade |
| --- | --- |
| 🧭 **Planejador** | Analisa o tema e define a estrutura e os principais tópicos do texto. |
| 🔎 **Pesquisador** | Busca informações relevantes na internet utilizando a API da Tavily. |
| ✍️ **Redator** | Utiliza o planejamento e as pesquisas para produzir o primeiro rascunho. |
| 🧐 **Crítico** | Analisa o texto produzido e identifica informações, dados ou pontos que precisam ser aprofundados. |
| 🔬 **Pesquisador Extra** | Realiza pesquisas específicas, utilizando Selenium, com base nas solicitações do crítico. |

Após a pesquisa adicional, as novas informações são utilizadas pelo redator para produzir uma **versão revisada e mais completa do texto**.

 ### 🔄 Fluxo do sistema

```
                    ┌───────────────┐
                    │     Tema      │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ 🧭 Planejador │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ 🔎 Pesquisador│
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │   ✍️ Redator  │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │   🧐 Crítico  │
                    └───────┬───────┘
                            │
                   Precisa de mais dados?
                         /       \
                       Sim       Não
                       │          │
                       ▼          ▼
              ┌──────────────┐  Finalização
              │ 🔬 Pesquisa  │
              │    Extra     │
              └──────┬───────┘
                     │
                     ▼
              ┌───────────────┐
              │ ✍️ Redator    │
              │    Revisão    │
              └───────┬───────┘
                      │
                      ▼
                📝 Texto Final
```

---

 ## 🛠️ Tecnologias utilizadas

 O projeto foi desenvolvido utilizando:

 - 🐍 **Python**
- 🤖 **Google Gemini 2.5** — geração e análise de texto
- 🧩 **LangGraph** — orquestração do fluxo de agentes
- 🔎 **Tavily** — pesquisa de informações na internet
- 🌐 **Selenium** — automação e pesquisa complementar na web
- 🎨 **Gradio** — interface web da aplicação
- 🔐 **python-dotenv** — gerenciamento das variáveis de ambiente

---

 ## 📋 Pré-requisitos

 Antes de começar, certifique-se de ter instalado:

 - **Python 3.10 ou superior**
- **Git**
- Um navegador compatível com o Selenium
- Uma chave de API do **Google Gemini**
- Uma chave de API do **Tavily**

---

 ## 🚀 Instalação

 ### 1\. Clone o repositório

```
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

 Entre na pasta do projeto:

```
cd SEU-REPOSITORIO
```

 ### 2\. Crie um ambiente virtual

 No Windows:

```
python -m venv venv
.\venv\Scripts\activate
```

 No Linux/macOS:

```
python3 -m venv venv
source venv/bin/activate
```

 ### 3\. Instale as dependências

```
pip install python-dotenv langgraph langchain-google-genai selenium tavily-python gradio
```

---

 ## 🔑 Configuração das APIs

 Crie um arquivo chamado `.env` na raiz do projeto:

```
GOOGLE_API_KEY="sua_chave_do_gemini_aqui"
TAVILY_API_KEY="sua_chave_do_tavily_aqui"
```

 > ⚠️ **Importante:** nunca compartilhe suas chaves de API publicamente e não faça commit do arquivo `.env` no GitHub.

 Recomenda-se adicionar o arquivo `.env` ao `.gitignore`:

```
.env
venv/
__pycache__/
*.pyc
```

---

 ## ▶️ Executando o projeto

 Com o ambiente virtual ativado, execute:

```
python main.py
```

 Após iniciar, o Gradio exibirá no terminal um endereço semelhante a:

```
http://127.0.0.1:7860
```

 Abra esse endereço no navegador para acessar a aplicação.

---

 ## 💡 Como utilizar

 1. Digite o **tema** sobre o qual deseja gerar o texto.
2. O agente planejador estrutura os principais pontos.
3. O pesquisador coleta informações relevantes.
4. O redator produz o primeiro rascunho.
5. O crítico analisa o conteúdo.
6. Caso sejam necessários dados adicionais, o pesquisador extra realiza novas buscas.
7. O redator utiliza as novas informações para revisar o texto.
8. O sistema apresenta o **resultado final**.

---

 ## 📁 Estrutura do projeto

```
SEU-REPOSITORIO/
│
├── main.py
├── README.md
├── 1.PNG
├── .env
├── .gitignore
└── venv/
```

 > O diretório `venv/` e o arquivo `.env` devem permanecer fora do controle de versão.

---

 ## 🔐 Segurança

 As chaves de API são informações sensíveis.

 **Nunca faça:**

```
git add .env
git commit -m "Adiciona chaves"
git push
```

 Utilize o `.gitignore` para impedir que credenciais sejam enviadas ao GitHub.

 Se uma chave for publicada acidentalmente, **revogue-a e gere uma nova chave** imediatamente.

---

 ## 📤 Enviando alterações para o GitHub

 Depois de atualizar o `README.md` ou qualquer outro arquivo:

```
git add README.md
```

 Crie um commit:

```
git commit -m "docs: atualiza README em português"
```

 Envie para o GitHub:

```
git push
```

 Se estiver enviando o projeto pela primeira vez:

```
git init
git add .
git commit -m "feat: adiciona equipe de agentes redatores"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
git push -u origin main
```

---

 ## 🎯 Objetivo

 O objetivo do projeto é demonstrar como uma arquitetura baseada em **múltiplos agentes de IA** pode dividir uma tarefa complexa em etapas especializadas, permitindo combinar:

 **Planejamento → Pesquisa → Redação → Crítica → Pesquisa complementar → Revisão**

 Essa abordagem pode ser adaptada para diferentes tipos de produção de conteúdo e fluxos de pesquisa automatizados.

---

 ## 🤝 Contribuição

 Contribuições são bem-vindas!

 Para contribuir:

 1. Faça um **fork** do projeto.
2. Crie uma branch para sua alteração.
3. Faça suas modificações.
4. Realize um commit descrevendo a alteração.
5. Envie um **Pull Request**.

---

 ## 📄 Licença

 Este projeto ainda não possui uma licença definida.

 Caso queira disponibilizar o código para uso e modificação por outras pessoas, considere adicionar uma licença, como a **MIT License**.

---

 ## ⭐ Gostou do projeto?

 Se este projeto foi útil ou interessante para você, considere deixar uma **estrela ⭐ no repositório** e acompanhar seu desenvolvimento.
