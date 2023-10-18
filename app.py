from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

import re

driver = webdriver.Chrome()
driver.get('https://www.mercadolivre.com.br/ofertas?container_id=MLB779535-1&domain_id=MLB-CELLPHONES#origin=scut&filter_applied=domain_id&filter_position=5&is_recommended_domain=false')

titulos = driver.find_elements(By.XPATH,"//p[@class='promotion-item__title']")

precos = driver.find_elements(By.XPATH,"//div[@class='andes-money-amount-combo__main-container']/span[@class='andes-money-amount andes-money-amount--cents-superscript']/span[@class='andes-money-amount__fraction']")

workbook = openpyxl.Workbook()

workbook.create_sheet('produtos')

sheet_produtos = workbook['produtos']
sheet_produtos['A1'].value = 'Produto'
sheet_produtos['B1'].value = 'Preço'

for titulo, preco in zip(titulos, precos):
    sheet_produtos.append([titulo.text, float(re.sub(r'[.]', '', preco.text))])

workbook.save('produtos.xlsx')