import pyautogui #bib. pyautogui
import time #bib. de tempo


#importante: antes de executar o arquivo, abrir um python debug console pressionando F5
#print(pyautogui.position())mostra a posição do mouse

#exibir mensagem de alerta
pyautogui.alert('O código irá a rodar, por favor não mexa em nada no mouse ou teclado')
pyautogui.PAUSE = 1.5 #esta função irá acrescentar meio segundo entre a execução de cada função

#PASSO 1: abrir o navegador
pyautogui.press('win')
pyautogui.write('brave')

pyautogui.press('enter')
time.sleep(2.5) #esta função acrescenta um tempo específico antes de continuar a rodar o código

#PASSO 2: abrir o google drive
pyautogui.write('https://drive.google.com/drive/u/0/my-drive')
pyautogui.press('enter')

#maximizar a tela
pyautogui.moveTo(x=785, y=24)
pyautogui.click()

#PASSO 3: pegar o arquivo da área de trabalho
pyautogui.hotkey('win', 'd') #função que combina teclas diferentes
pyautogui.moveTo(857,631)#função para arrastar o mouse
pyautogui.mouseDown()#clickar e PRESSIONAR esquerdo do mouse

#PASSO 4: arrastar até o google drive
pyautogui.moveTo(x=738, y=594)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.mouseUp()

#PASSO 5: esperar fazer o upload do arquivo e finalizar o código
time.sleep(1)
pyautogui.alert('O código foi finalizado, pode voltar a sua rotina')