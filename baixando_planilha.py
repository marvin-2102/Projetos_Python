from selenium import webdriver
from time import sleep

#Baixando os dados

# Entrando no site e esperando
driver = webdriver.Opera()
driver.get(' https://br.investing.com/currencies/usd-brl-historical-data')
sleep(2)

# Aceitando o pop-up
driver.find_element_by_id('onetrust-accept-btn-handler').click()
sleep(2)
# Entrando na conta
driver.find_element_by_link_text('Baixar dados').click()
# Email
email = driver.find_element_by_id('loginFormUser_email')
email.send_keys('email')
# Senha
senha = driver.find_element_by_id('loginForm_password')
senha.send_keys('senha')
# Entrando
botoes_login = driver.find_elements_by_css_selector('a.orange')#Encontrando todos os botões laranjas
botoes_login[2].click()#Atravês de testes foi descoberto que o botão da posição '2' era o botão desejado

# Por fim, baixando devidamente os dados
driver.find_element_by_link_text('Baixar dados').click()