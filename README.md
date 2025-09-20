# AI-API: Integração com Modelos de Linguagem

[![Python](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.103.2-009688.svg?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/status-ativo-success.svg?style=for-the-badge)]()

Uma API robusta e escalável construída com Python e FastAPI para servir como uma interface de comunicação com grandes modelos de linguagem (LLMs), como o Google Gemini. Este projeto foi desenvolvido seguindo as melhores práticas de engenharia de software, incluindo uma arquitetura modular, gerenciamento seguro de configurações e documentação interativa.

---

## ✨ Features

-   **Integração com IA Generativa**: Conecta-se diretamente com a API do Google Gemini para processamento de linguagem natural.
-   **Endpoint de Chat**: Rota `/api/v1/chat` para enviar prompts e receber respostas em tempo real.
-   **Documentação Automática**: Geração automática de documentação interativa com Swagger UI (`/docs`) e ReDoc (`/redoc`).
-   **Estrutura Profissional**: Código organizado com separação de responsabilidades (API, serviços, schemas).
-   **Configuração Segura**: Gerenciamento de chaves de API através de variáveis de ambiente com `.env`.
-   **Página de Status Elegante**: Endpoint raiz (`/`) com uma página de status moderna e informativa.

---

## 🛠️ Tecnologia Utilizada

-   **Python 3.12+**
-   **FastAPI**: Framework web de alta performance para a construção da API.
-   **Uvicorn**: Servidor ASGI para rodar a aplicação.
-   **Google Generative AI**: SDK oficial do Google para interagir com o Gemini.
-   **Pydantic**: Para validação de dados e gerenciamento de configurações.
-   **PyYAML**: Para carregar configurações de arquivos YAML.
-   **Pytz**: Para manipulação de fusos horários.

---

## 🚀 Começando

Siga estas instruções para obter uma cópia do projeto e executá-lo em sua máquina local.

### Pré-requisitos

-   [Python 3.12 ou superior](https://www.python.org/downloads/)
-   [Git](https://git-scm.com/)
-   Uma chave de API do [Google AI Studio](https://aistudio.google.com/app/apikey)

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/AI-API.git](https://github.com/seu-usuario/AI-API.git)
    cd AI-API
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

---

## ⚙️ Configuração

1.  **Crie um arquivo `.env` a partir do exemplo:**
    ```bash
    cp .env.example .env
    ```

2.  **Adicione sua chave de API:**
    Abra o arquivo `.env` e insira sua chave do Google API Key que você gerou.
    ```env
    GOOGLE_API_KEY="SUA_CHAVE_API_SUPER_SECRETA_AQUI"
    ```

---

## ▶️ Executando a API

Com o ambiente virtual ativado, inicie o servidor Uvicorn:

```bash
uvicorn app.main:app --reload
```

-   O servidor estará disponível em `http://127.0.0.1:8000`.
-   A flag `--reload` reinicia o servidor automaticamente após qualquer alteração no código.

Acesse [http://127.0.0.1:8000](http://127.0.0.1:8000) no seu navegador para ver a página de status ou [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para interagir com a API.

---

## Endpoints da API

### `POST /api/v1/chat`

Envia uma mensagem para o modelo de IA e retorna sua resposta.

**Request Body:**
```json
{
  "message": "Qual a capital de Pernambuco?"
}
```

**Exemplo com cURL:**
```bash
curl -X 'POST' \
  '[http://127.0.0.1:8000/api/v1/chat](http://127.0.0.1:8000/api/v1/chat)' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "message": "Qual a capital de Pernambuco?"
}'
```

**Success Response (200 OK):**
```json
{
  "reply": "A capital de Pernambuco é Recife."
}
```

---

## 📂 Estrutura do Projeto

```
/AI-API
|
├── .env                  # Armazena as chaves de API (local, não versionado)
├── .env.example          # Arquivo de exemplo para as variáveis de ambiente
├── .gitignore            # Arquivos e pastas a serem ignorados pelo Git
├── README.md             # Este arquivo
├── requirements.txt      # Dependências do projeto Python
|
└── app/
    ├── __init__.py       # Inicializador do módulo 'app'
    ├── api.py            # Definição dos endpoints da API (rotas)
    ├── main.py           # Ponto de entrada da aplicação FastAPI
    ├── schemas.py        # Schemas Pydantic para validação de dados
    └── services.py       # Lógica de negócio e comunicação com serviços externos (IA)
```

---

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.