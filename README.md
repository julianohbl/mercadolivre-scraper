# Extração de Dados do Mercado Livre

Este código em Python é uma demonstração de como utilizar a biblioteca Selenium para extrair informações de uma página da web, no caso, o site do Mercado Livre. Ele também faz uso da biblioteca openpyxl para criar uma planilha no formato XLSX e salvar os dados extraídos nessa planilha.

## Requisitos

Antes de executar este código, é importante garantir que você tenha as seguintes bibliotecas instaladas no seu ambiente Python:

- [Selenium](https://selenium-python.readthedocs.io/): Esta biblioteca é utilizada para automatizar a interação com o navegador e extrair informações de páginas da web.
- [Openpyxl](https://openpyxl.readthedocs.io/en/stable/): Ela é responsável pela criação e manipulação de planilhas Excel.

Além disso, você deve ter o ChromeDriver instalado e configurado corretamente para que o Selenium funcione com o Google Chrome. Certifique-se de que o caminho do ChromeDriver esteja configurado de acordo com o seu ambiente.

## Funcionamento do Código

Aqui está uma análise passo a passo do que o código faz:

1. **Importação de Bibliotecas**: O código começa importando as bibliotecas necessárias, incluindo `selenium`, `openpyxl`, e `re` (para manipulação de expressões regulares).

2. **Inicialização do Selenium**: O código inicia uma instância do navegador Google Chrome utilizando o WebDriver do Selenium.

3. **Navegação para a Página**: O navegador é direcionado para a página de ofertas de celulares do Mercado Livre.

4. **Extração de Dados**:
   - `titulos` recebe todos os elementos HTML que contêm os títulos dos produtos.
   - `precos` recebe todos os elementos HTML que contêm os preços dos produtos.

5. **Criação da Planilha Excel**:
   - Um arquivo Excel é criado utilizando a biblioteca openpyxl.
   - Uma planilha chamada 'produtos' é criada no arquivo.

6. **Cabeçalho da Planilha**: São adicionados os títulos 'Produto' e 'Preço' nas células A1 e B1, respectivamente.

7. **Inserção de Dados na Planilha**: O código utiliza um loop para iterar sobre os títulos e preços coletados, inserindo-os na planilha. Os preços são tratados para remover possíveis pontos de milhar, sendo convertidos em valores numéricos.

8. **Salvamento da Planilha**: A planilha é salva no arquivo 'produtos.xlsx'.

## Utilização

Para executar o código:

1. Garanta que todas as bibliotecas necessárias estejam instaladas.
2. Configure o ChromeDriver para o seu ambiente.
3. Execute o código.

Após a execução, você terá um arquivo 'produtos.xlsx' contendo os títulos e preços dos produtos listados na página de ofertas de celulares do Mercado Livre.
