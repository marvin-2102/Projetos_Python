import os

# Cria o arquivo bg.text
def cria_bg():

    for file_type in ['neg']:
        for img in os.listdir(file_type):
            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat', 'a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('arquivosSamples/bg.txt', 'a') as f:
                    f.write(line)
cria_bg()
