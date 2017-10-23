# coding: utf-8

from selenium import webdriver

browser = webdriver.Firefox(
    executable_path=r'D:\RepositoriosWesley\scrapSelenium\geckodriver.exe')

browser.get('http://www.sefaz.go.gov.br/ccn/')

''' Seleciona o Tipo de Documento para Consulta '''
radio = browser.find_element_by_css_selector(
    'div.col-sm-3:nth-child(2) > label:nth-child(1) > input:nth-child(1)')

radio.click()

''' Informa o Numero do CNPJ '''
cnpj = '03928932000197'
elem = browser.find_element_by_xpath('//*[@id="numrDocumento"]')
elem.clear()
elem.send_keys(cnpj)

''' Envia a Requisição '''
browser.find_element_by_xpath('//*[@id="btnSubmit"]').click()


''' Acessar o Resultado'''
browser.switch_to.default_content()

browser.switch_to.frame('Result')

table = browser.find_elements_by_css_selector('.table >tbody:nth-child(2)')

for tr in table:
    incricao_estadual = tr.find_element_by_css_selector(
        '.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1)')
    situacao_cadastro = tr.find_element_by_css_selector(
        '.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)')
    # printar informações
    print("""IE: {ie}, \nSituação Cadastral: {situacao}""".format(
        ie=incricao_estadual.text,
        situacao=situacao_cadastro.text
    ))

browser.quit()
