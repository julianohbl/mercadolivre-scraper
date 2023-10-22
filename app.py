from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import openpyxl
import time
import re

def setup_driver(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

def create_workbook():
    workbook = openpyxl.Workbook()
    sheet_produtos = workbook.active
    sheet_produtos.title = 'produtos'
    sheet_produtos['A1'] = 'Produto'
    sheet_produtos['B1'] = 'Preço'
    return workbook, sheet_produtos

def click_cookie_consent(driver):
    cookie_consent_button = driver.find_elements(By.CLASS_NAME, "cookie-consent-banner-opt-out__container")
    if cookie_consent_button:
        cookie_consent_button[0].click()

def scrape_data(driver, sheet_produtos):
    titulos = driver.find_elements(By.XPATH, "//p[@class='promotion-item__title']")
    precos = driver.find_elements(By.XPATH, "//div[@class='andes-money-amount-combo__main-container']/span[@class='andes-money-amount andes-money-amount--cents-superscript']/span[@class='andes-money-amount__fraction']")

    for titulo, preco in zip(titulos, precos):
        sheet_produtos.append([titulo.text, float(re.sub(r'[.]', '', preco.text))])
        print([titulo.text, preco.text])

def main():
    url = 'https://www.mercadolivre.com.br/ofertas?container_id=MLB779535-1&domain_id=MLB-CELLPHONES#origin=scut&filter_applied=domain_id&filter_position=5&is_recommended_domain=false'

    driver = setup_driver(url)
    workbook, sheet_produtos = create_workbook()

    while True:
        click_cookie_consent(driver)
        scrape_data(driver, sheet_produtos)

        try:
            driver.find_element(By.XPATH, "//li[@class='andes-pagination__button andes-pagination__button--next andes-pagination__button--disabled']")
            print("Elemento 'final' encontrado. Parando o loop.")
            break
        except NoSuchElementException:
            pass

        nova_pagina = driver.find_element(By.XPATH, "//li[@class='andes-pagination__button andes-pagination__button--next']/a")
        nova_pagina.click()
        time.sleep(3)

    workbook.save('produtos.xlsx')
    driver.quit()

if __name__ == "__main__":
    main()