import time
import pyautogui
import pyperclip

time.sleep(5)
#posição do mouse
po = pyautogui.position()
#imprimindo a posição do mouse
print(po)

#clicando na posição(abrindo chrome)
pyautogui.click(x=756, y=757, clicks=2)
#aguardadndo 5 segundos
time.sleep(5)
#copiando endereço de email
pyperclip.copy("https://google.com")
#colando endereço de email
pyautogui.hotkey("ctrl","v")
#pressionando enter
pyautogui.press("enter")