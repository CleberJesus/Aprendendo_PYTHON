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

#tempo de espera entre comandos
pyautogui.PAUSE = 3

#abrir o chrome
pyautogui.hotkey("ctrl", "w")

#abrir nova aba navegador
pyautogui.hotkey("ctrl","t")
#copiando endereco resolvendo carcteres especiais
pyperclip.copy("https://drive.google.com/drive/folders/12254455....")
#colando no navegador
pyautogui.hotkey("ctrl","v")
#pressionando enter
pyautogui.press("enter")

#esperando 5 segundos
time.sleep(5)
#navegar no sistema e encontrar a base de dados
#exportar/download base de dados
#importar a base de dados para o python
#basededados.py
#calcular os indicadores
#basededados.py

#enviar um email para diretoria com relatorio
#abrir o email(link: https://mail...endereço de email)
pyautogui.hotkey("ctrl","t") #abrir nova aba
pyautogui.copy("https://mail...endereço de email")
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")
time.sleep(7)

#clicar no escrever
pyautogui.click(x=256,y=431)
time.sleep(2)

#escrever o email destinatário
pyautogui.write("emaildestinatario@mail.com")
pyautogui.press("tab") #seleciona o destinatário
pyaitogui.press("tab") #passar para o campo assunto

#escrever o assunto
pyperclip.copy("Relatório de vendas")
pyautogui.write("ctrl","v")
pyautogui.press("tab")

#escreve o corpo do email
texto = f'''
Prezados, bom dia.
O faturamento de ontem foi de : R$ {faturamento:,.2}
A quantidade de produtos foi de : {quantidade:,}
Atenciosamente 
'''
pyperclip.copy(texto)
pyautogui.hotkey("ctrl","v")


#enviar o email
pyautogui.hotkey("ctrl","enter")
