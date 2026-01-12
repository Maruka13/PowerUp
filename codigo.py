# passo 1: entrar no sistema da empresa 
# passo 2: fazer login
# passo 3: abrir base de dados
# passo 4: cadastrar um produto
# passo 5: repetir o passo 4 ate acabar a lista de produtos

import pyautogui

pyautogui.PAUSE = 0.5

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")       # pyautogui.hotkey("command", "space") # macOS
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")

