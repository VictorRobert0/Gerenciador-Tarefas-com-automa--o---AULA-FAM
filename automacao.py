import pyautogui
import time


#.press "Apertar alguma tecla"
#.write"Escrever algo"

pyautogui.PAUSE = 0.3


pyautogui.press('win')
pyautogui.sleep(2)
pyautogui.write('geren')
pyautogui.sleep(2)
pyautogui.press('enter')
pyautogui.sleep(2)
pyautogui.press('down')
pyautogui.sleep(1)
pyautogui.press('down')
pyautogui.sleep(1)
pyautogui.press('enter')

#AGUARDAR O SISTEMA DE EMPRESA ABRIR

pyautogui.sleep(7)

#INSERIR TAREFA

pyautogui.write('PANDAS')
pyautogui.sleep(1)
pyautogui.press('tab')
pyautogui.sleep(1)
pyautogui.press('space')



#- importar a base de dados dos produtos
import pandas 

tabela = pandas.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:

    #CLICK PARA INSERIR CADASTRO NOVO
    pyautogui.click(x=494, y=328)

    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]

    pyautogui.sleep(2)
    pyautogui.write(str(codigo))
    pyautogui.sleep(2)
    pyautogui.write(str(marca))


    #inserir um cadastro do banco de dados


    #CLICK NO BOTAO
    pyautogui.click(x=744, y=327)

    pyautogui.sleep(2)



