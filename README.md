# Extração de Dados do Mercado Livre

Este código em Python é uma demonstração de como utilizar a biblioteca Selenium para extrair informações de uma página da web, no caso, o site do Mercado Livre. Ele também faz uso da biblioteca openpyxl para criar uma planilha no formato XLSX e salvar os dados extraídos nessa planilha.

## Requisitos

Antes de executar este código, é importante garantir que você tenha as seguintes bibliotecas instaladas no seu ambiente Python:

- [Selenium](https://selenium-python.readthedocs.io/): Esta biblioteca é utilizada para automatizar a interação com o navegador e extrair informações de páginas da web.
- [Openpyxl](https://openpyxl.readthedocs.io/en/stable/): Ela é responsável pela criação e manipulação de planilhas Excel.

Além disso, você deve ter o ChromeDriver instalado e configurado corretamente para que o Selenium funcione com o Google Chrome. Certifique-se de que o caminho do ChromeDriver esteja configurado de acordo com o seu ambiente.

## Funcionalidades

1. **Acesso ao Site**: O script acessa a página de ofertas de celulares no Mercado Livre.

2. **Coleta de Dados**: Ele extrai informações dos produtos, incluindo o título e o preço.

3. **Manipulação de Cookies**: Lida com banners de consentimento de cookies, caso estejam presentes na página.

4. **Armazenamento em Excel**: Os dados coletados são armazenados em um arquivo Excel com duas colunas: "Produto" e "Preço".

5. **Navegação em Páginas**: O scraper verifica se há mais páginas de ofertas e navega por elas até que não haja mais páginas a serem coletadas.

## Utilização

1. **Execução**: Execute o script com o comando `python app.py`. Ele iniciará o navegador, coletará dados e salvará em um arquivo Excel.

2. **Personalização**: O código pode ser personalizado para coletar informações específicas ou automatizar outras tarefas no site.


Após a execução, você terá um arquivo 'produtos.xlsx' contendo os títulos e preços dos produtos listados na página de ofertas de celulares do Mercado Livre.

## Notas

- Respeite os termos de serviço do Mercado Livre e evite sobrecarregar o site com solicitações excessivas.
- Este projeto é fornecido sob a licença MIT (consulte o arquivo `LICENSE`).
