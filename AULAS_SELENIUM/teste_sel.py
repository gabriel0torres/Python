from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui as gui

gui.alert('O código irá rodar! Por favor, não mexa no teclado e mouse enquanto não exibir a mensagem de sucesso.')
navegador = webdriver.Chrome(ChromeDriverManager().install())
#LEIA AS ANOTAÇÕES

#pegando o demonstrativo da petrobras
#navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get("https://www.investidorpetrobras.com.br/")
navegador.find_element( "xpath", '//*[@id="lang-pt-br"]/div[1]/div[1]/div/div[4]/ul[1]/li/a').click()
time.sleep(6)
button = navegador.find_element("xpath", '//*[@id="lang-pt-br"]/div[8]/div')
navegador.execute_script("arguments[0].click();", button)
#navegador.find_element( "xpath", '//*[@id="tabela_1"]/tr[10]/td[3]/a').click()
button = navegador.find_element("xpath", '//*[@id="tabela_1"]/tr[10]/td[3]/a')
navegador.execute_script("arguments[0].click();", button)
#time.sleep(1)


#pegando o demonstrativo da americanas
navegador.get("https://ri.americanas.io/")
navegador.find_element( "xpath", '//*[@id="lang-pt-br"]/div[2]/div/div').click()
navegador.find_element("xpath", '//*[@id="lang-pt-br"]/main/section/div[2]/div/div/div[2]/a').click()

gui.alert('Código Rodado com sucesso! Pode voltar a sua rotina.')