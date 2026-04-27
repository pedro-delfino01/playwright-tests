* Passo a Passo - Playwright *

1. Instalação
- Instalar Python (vocês já sabem)

- Criar venv no diretório de testes
|_ python -m venv venv
|_ venv\Scripts\activate
** Se não ativar, utilizar o comando abaixo e depois tentar ativar novamente:
|_ Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
|_ venv\Scripts\activate

- Instalar Playwright e Pytest
|_ pip install playwright
|_ pip install pytest-playwright

- Instalar browsers (Chromium, Firefox e Webkit (Safari))
|_ playwright install

2. Como executar esses testes
    2.1. Um arquivo inteiro:
    |_ pytest [nome do arquivo]
    2.2. Um teste específico:
    |_ pytest -k [nome do teste]
    2.3. Testes no modo headed (o normal é rodar no modo headless):
    |_ pytest --headed
    2.4. Teste em um navegador específico (o normal é rodar no Chromium):
    |_ pytest --browser webkit

3. Como visualizar logs de execução
    3.1. Primeiramente, é necessário habilitar o "trace viewer", ou
    o "visualizador de traços" ao executar os testes:
    |_ pytest --tracing on
    ** Existem 3 opções para o trace viewer: on (ativo), off (inativo) e
... retain-on-failure (grava todos os testes, mas remove todos os testes
    que passaram e mantém os que deram erro)
    *** É necessário estar com o pytest instalado (cado dê erro, instale o pytest-playwright)
    3.2. Para visualizar o Trace Viewer de um teste específico, primeiro
    verifique se foi criado o arquivo referente ao teste:
    ** Nesse caso, um dos arquivos gerado foi "test-results\tests-test-login-py-test-positivelogin-chromium\trace.zip"
    3.3. Para visualizar o arquivo, utilize o comando abaixo:
    |_ playwright show-trace [caminho_ate_o_arquivo]\trace.zip
