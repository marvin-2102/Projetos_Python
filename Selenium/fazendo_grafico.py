import pandas as pd
import matplotlib.pyplot as plt

#Lendo o arquivo e fazendo um gráfico

cotacao_df = pd.read_csv(r'USD_BRL Dados Históricos.csv')
display(cotacao_df)
# Trasnormando a coluna data para ter apenas os dias

for item, dia in enumerate(cotacao_df['Data']):
    cotacao_df['Data'][item] = cotacao_df['Data'][item][0:2]
    
display(cotacao_df)

data_dia = [dia for dia in cotacao_df['Data']]
maxima_cotacao = [maxima for maxima in cotacao_df['Máxima']]
minima_cotacao = [minima for minima in cotacao_df['Mínima']]
variacao_cotacao = [variacao for variacao in cotacao_df['Var%']]

# Invertendo as listas
variacao_cotacao.sort(reverse=True)

plt.figure(figsize=(14, 14))
plt.title('Cotação Dolár-Real, de 25.05.2021 até 26.06.2021')
plt.xlabel('Dias')
plt.ylabel('Valores')
plt.grid(True)
plt.plot(data_dia, minima_cotacao, 'ro')
plt.plot(data_dia, maxima_cotacao, 'go')

plt.legend(('Valor Mínimo',' Valor Máximo'), loc='upper left')

plt.show()

plt.figure(figsize=(14, 12))
plt.title('Varição Percentual')
plt.xlabel('Data')
plt.ylabel('Variação')
plt.grid(True)
plt.plot(data_dia, variacao_cotacao, 'b')