populacao = 7000000000
a1 = 10
an = a1
soma = 0
count_days = 1
while soma < populacao:
    soma += an   
    termo_geral = an*4 + an
    an = termo_geral
    count_days += 1
print(count_days)  
