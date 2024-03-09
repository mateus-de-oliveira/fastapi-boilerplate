# Configuração do Ambiente de Desenvolvimento

Este boilerplate já vem preparado com tudo o que você precisa para começar a trabalhar em uma aplicação FastAPI, assegurando qualidade e padronização de código com o Pylint e Pre-Commit. Aqui estão as instruções para configurar seu ambiente e instalar as dependências.

## 🐍 Configuração do Ambiente Virtual

Isolar as dependências do projeto em um ambiente virtual é essencial. Siga os passos abaixo para configurá-lo:

1. **Se ainda não tiver o Virtualenv instalado:**
    ```bash
    pip install virtualenv
    ```
2. **Na raiz do projeto, crie o ambiente virtual:**
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

Ative seu ambiente virtual para instalar as dependências do `requirements.txt`.

1. **Com o ambiente virtual ativo, instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

## 🔗 Configurando o Pre-Commit

Com as dependências instaladas, configure o Pre-Commit para automatizar a checagem de código.

1. **Execute o Pre-Commit:**
    ```bash
    pre-commit install
    ```

Este comando configurará o Pre-Commit para ser executado antes de cada commit, garantindo que seu código esteja alinhado com as regras definidas.

## 🔨 Uso

Para iniciar o desenvolvimento, ative o ambiente virtual e inicie o servidor com o Uvicorn:

1. **Ative o ambiente virtual, se necessário:**
    ```bash
    source venv/bin/activate  # Linux/Mac
    .\venv\Scripts\activate  # Windows
    ```
2. **Inicie o servidor FastAPI:**
    ```bash
    uvicorn src.main:app --reload
    ```

O arquivo `src/main.py` deve conter a aplicação FastAPI. A flag `--reload` faz com que o servidor reinicie automaticamente ao detectar alterações no código, facilitando o desenvolvimento.

Agora, com o ambiente configurado e o servidor rodando, você pode começar a codificar com confiança, sabendo que suas contribuições estarão consistentes e de qualidade!
