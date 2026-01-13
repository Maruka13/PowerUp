# passo 1: entrar no sistema da empresa 
# passo 2: fazer login
# passo 3: abrir base de dados
# passo 4: cadastrar um produto
# passo 5: repetir o passo 4 ate acabar a lista de produtos

import pyautogui
import time

pyautogui.PAUSE = 0.5 # pausa entre scripts

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")       # pyautogui.hotkey("command", "space") # macOS
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(3)

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3) # pausa especifica para esperar a pagina carregar

pyautogui.click(x=694, y=373) # posição do mouse na tela de login
pyautogui.write("manugomes@gmail.com")
pyautogui.press("tab") # pula para senha
pyautogui.write("senha deveras dificil")
pyautogui.press("tab") # pula pro botao
pyautogui.press("enter")
time.sleep(5)

# pip install pandas openpyxl

import pandas

tabela = pandas.read_csv("produtos.csv")