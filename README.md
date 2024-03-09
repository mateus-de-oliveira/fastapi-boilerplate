# Configuração do Ambiente de Desenvolvimento

Este boilerplate inclui tudo o que você precisa para começar a trabalhar em uma aplicação FastAPI com qualidade e padronização de código asseguradas pelo Pylint, com as configurações de pre-commit já estabelecidas. Siga os passos abaixo para configurar seu ambiente virtual e instalar todas as dependências necessárias.

## 🐍 Configuração do Ambiente Virtual

Para isolar suas dependências e manter a consistência entre os ambientes de desenvolvimento, recomendamos a utilização de um ambiente virtual Python. Veja como configurá-lo:

1. **Instale o Virtualenv, se ainda não o tiver:**
    ```bash
    pip install virtualenv
    ```
2. **Na raiz do projeto, crie seu ambiente virtual:**
    ```bash
    virtualenv venv
    ```
3. **Ative o ambiente virtual:**
    - **No Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    - **No Linux ou Mac:**
        ```bash
        source venv/bin/activate
        ```

## 📦 Instalando Dependências

Com o ambiente virtual ativo, instale as dependências do projeto contidas no arquivo `requirements.txt`.

1. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

Agora você está pronto para começar a desenvolver com todas as ferramentas e extensões necessárias já configuradas no template! 🚀

## 🔨 Uso

Para começar a trabalhar em sua aplicação FastAPI, assegure-se de que o ambiente virtual esteja ativo e utilize o Uvicorn para rodar o servidor:

1. **Ative o ambiente virtual:**
    ```bash
    # Se ainda não estiver ativo
    source venv/bin/activate  # Linux/Mac
    .\venv\Scripts\activate  # Windows
    ```
2. **Execute a aplicação:**
    ```bash
    uvicorn src.main:app --reload
    ```

O comando acima assume que sua aplicação FastAPI está definida no arquivo `src/main.py`. A flag `--reload` é útil durante o desenvolvimento, pois permite que o servidor reinicie automaticamente após mudanças no código.
