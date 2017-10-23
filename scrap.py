# coding: utf-8

from selenium import webdriver

browser = webdriver.Firefox()

browser.get('http://www.sefaz.go.gov.br/ccn/')

''' Seleciona o Tipo de Documento para Consulta '''
radio = browser.find_element_by_css_selector(
    'div.col-sm-3:nth-child(2) > label:nth-child(1) > input:nth-child(1)')

radio.click()

''' Informa o Numero do CNPJ '''
cnpj = '77500049000308'
elem = browser.find_element_by_xpath('//*[@id="numrDocumento"]')
elem.clear()
elem.send_keys(cnpj)

''' Envia a Requisição '''
browser.find_element_by_xpath('//*[@id="btnSubmit"]').click()


''' Acessar o Resultado'''
browser.switch_to.default_content()

browser.switch_to.frame('Result')

rows = browser.find_elements_by_css_selector('.table > tbody:nth-child(2) > tr')
for tr in rows:
    incricao_estadual = tr.find_element_by_css_selector('td:nth-child(1)')
    situacao_cadastro = tr.find_element_by_css_selector('td:nth-child(2)')
    uf = tr.find_element_by_css_selector('td:nth-child(3)')
    nome_fantasia = tr.find_element_by_css_selector('td:nth-child(5)')
    razao_social = tr.find_element_by_css_selector('td:nth-child(6)')

    ''' Printar as informações da Consulta'''
    print("""-.-.-.-.-.-.-.-.-.-.-.-.-.-\nRazão Social: {razao}\nFantasia: {fantasia}
    \nUF: {uf} - IE: {ie}, Situação Cadastral: {situacao}\n""".format(
        razao=razao_social.text,
        fantasia=nome_fantasia.text,
        uf=uf.text,
        ie=incricao_estadual.text,
        situacao=situacao_cadastro.text,
    ))

browser.quit()

