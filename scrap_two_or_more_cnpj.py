# coding: utf-8

from selenium import webdriver

browser = webdriver.Firefox()
''' Site para Pesquisa de Cadastro de Contribuintes Nacional '''
browser.get('http://www.sefaz.go.gov.br/ccn/')

empresas = ['13481309010155', '77500049000308', '00776574000660',
            '01534080000128', '03007331000141']

''' Informa o Numero do CNPJ '''
for cnpj in empresas:

    browser.switch_to.default_content()

    ''' Seleciona o Tipo de Documento para Consulta  = CNPJ'''
    radio = browser.find_element_by_css_selector(
        'div.col-sm-3:nth-child(2) > label:nth-child(1) > input:nth-child(1)')
    browser.implicitly_wait(1)

    radio.click()

    elem = browser.find_element_by_xpath('//*[@id="numrDocumento"]')
    elem.clear()
    elem.send_keys(cnpj)

    ''' Envia a Requisição '''
    browser.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    browser.implicitly_wait(1)

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
