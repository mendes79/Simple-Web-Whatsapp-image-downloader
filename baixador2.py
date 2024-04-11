import pyautogui as gui
import time
import sys
import os

# Enter the folder location where the downloaded images should be saved
caminho = r"C:\Users\mende\Documents\Python\04-Baixa_Imagens\baixadas"

# My setup has 3 monitors and I choose which monitor the WhatsApp web window is open on.
# Change to the x and y coordinates of the center of your monitor.
tela = int(input(
    "Digite qual a tela: [1] Notebook, [2] Monitor Samsung OU [3] Samsung 2: "))
if tela == 1:
    x = 945
    y = 530
    monitor = "na tela do Notebook."
else:
    if tela == 2:
        x = 2865
        y = 286
        monitor = "no monitor Samsung."
    elif tela == 3:
        x = 4795
        y = 286
        monitor = "no monitor Samsung 2 (3a tela)."
    else:
        print("Opção inválida, rode novamente e escolha corretamente o monitor do web whatsapp.")
        sys.exit()

# number of images to download
qtd = int(input("Digite a quantidade de fotos a baixar (maior que zero): "))
if qtd < 1:
    print("A quantidade de fotos a baixar deve ser interira e maior que 0...")
    sys.exit()

time.sleep(3)
gui.moveTo(x, y, 1.5)
gui.click(button='right')
gui.press('down')
time.sleep(0.3)
gui.press('down')
time.sleep(0.3)
gui.press('enter')
time.sleep(0.3)
gui.press('tab')
time.sleep(0.15)
gui.press('tab')
time.sleep(0.15)
gui.press('tab')
time.sleep(0.15)
gui.press('tab')
time.sleep(0.15)
gui.press('tab')
time.sleep(0.15)
gui.press('tab')
time.sleep(0.15)
gui.press('enter')
time.sleep(0.5)
gui.write(caminho)
time.sleep(2)
gui.press('enter')
time.sleep(0.5)
gui.press('tab')
time.sleep(0.15)
gui.press('tab')
time.sleep(0.15)
gui.press('tab')
time.sleep(0.15)
gui.press('tab')
time.sleep(0.15)
gui.press('tab')
time.sleep(0.15)
gui.press('tab')
time.sleep(0.15)
gui.press('tab')
time.sleep(0.15)
gui.press('tab')
time.sleep(0.15)
gui.press('enter')
time.sleep(1.5)
print(f"Imagem-{qtd} salva")
contagem = qtd-1
print(contagem)
gui.click(x=x, y=y)
time.sleep(0.3)
gui.click(x=x, y=y)
time.sleep(1)

while contagem > 0:
    # gui.click(x=x,y=y)
    # time.sleep(0.3)
    # gui.click(x=x,y=y)
    # time.sleep(0.3)
    time.sleep(0.5)
    gui.press('right')
    time.sleep(1.5)
    gui.click(button='right')
    time.sleep(1)
    gui.press('down')
    time.sleep(0.3)
    gui.press('down')
    time.sleep(0.3)
    # gui.press('down')
    # time.sleep(0.5)
    gui.press('enter')
    time.sleep(1)
    gui.press('enter')
    time.sleep(2)
    print(f"Imagem-{contagem} salva")
    gui.click(x=x, y=y)
    time.sleep(0.5)
    gui.click(x=x, y=y)
    time.sleep(0.5)
    contagem = contagem-1
print(f"As {qtd} fotos foram salvas na pasta baixadas...")
gui.alert(text=f'As {qtd} fotos foram salvas na pasta baixadas!',
          title='Concluído', button='OK')
