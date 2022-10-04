import os
import shutil
import pyautogui as gui
from webbrowser import Chrome
from selenium import webdriver 
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

gui.alert('O código irá rodar')

pasta = "downloadarquivo"
dir = "C:/diretorio"
if os.path.exists(r"C:\diretorio"):
    shutil.rmtree(os.path.join(dir, pasta))

download_dir = r"C:\diretorio"

opt = webdriver.ChromeOptions()
opt.add_argument("--headless")
opt.add_experimental_option('prefs', {
        #"plugins.plugins_list": [{"enabled":False,"name":"Chrome PDF Viewer"}],
        "download": {
        "prompt_for_download": False,
        "default_directory"  : download_dir
        }
    })

services = Service(ChromeDriverManager().install())
services.creationflags = CREATE_NO_WINDOW

navegador = webdriver.Chrome(service=services,options=opt)
navegador.maximize_window()
navegador.get("link")

sleep(5)

folder = r"C:\diretorio\\"

for file_name in os.listdir(folder):
    old_name = folder + file_name
    new_name = folder + 'arquivo.csv'
    os.rename(old_name, new_name)

gui.alert('Código rodado com sucesso')