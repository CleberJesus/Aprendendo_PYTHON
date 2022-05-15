import pyautogui
import pyperclip

#tempo de espera entre comandos
pyautogui.PAUSE = 3

#abrir chrome atalho
pyautogui.hotkey("ctrl", "w")

#abrir chrome botao windows
pyautogui.press("win")
pyperclip.copy("chrome")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")