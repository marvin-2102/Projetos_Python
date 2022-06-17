from pathlib import Path
from shutil import move

#Agora vamos pegar esses dados no campo de downloads

caminho = Path('C:/Users/marki/Downloads/USD_BRL Dados Históricos.csv')
novo_caminho = Path('C:/Users/marki/Documents/Selenium_Modulo/USD_BRL Dados Históricos.csv')

move(caminho, novo_caminho)