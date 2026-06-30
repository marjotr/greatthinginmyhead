# 🤖 Assistente Virtual com Google AI

Este é um assistente inteligente desenvolvido em Python que utiliza os modelos de Inteligência Artificial do **Google AI** (Gemini) para processar interações e responder a comandos.

## 🚀 Funcionalidades

* 🧠 Geração de respostas inteligentes utilizando modelos do Google.
* 💬 Interface simplificada via terminal para interagir com o assistente.
* 🔒 Gerenciamento seguro de credenciais locais.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Google GenAI SDK** (Biblioteca oficial do Google AI)
* **Git & GitHub** (Para controle de versão)

## 📦 Como Instalar e Rodar o Projeto

Siga os passos abaixo para configurar e testar o projeto na sua máquina:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/marjotr/greatthinginmyhead.git
   ```

2. **Configure as Variáveis de Ambiente:**
   * Crie um arquivo chamado `.env` na raiz do projeto.
   * Adicione a sua chave do Google AI dentro dele:
     ```text
     GEMINI_API_KEY=sua_chave_do_google_aqui
     ```
   *(⚠️ O arquivo `.env` está listado no `.gitignore` e nunca será enviado para o GitHub por motivos de segurança).*

3. **Execute o assistente:**
   ```bash
   python assistente.py
   ```