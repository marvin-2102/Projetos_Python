from ContasBanco import ContaCorrente, CartaoCredito#Importando as Classes do arquivo exercício_banco
from Agencia import AgenciaComum, AgenciaPremium, AgenciaVirtual

cliente = ContaCorrente("João", 123131, 2123123, 343224)
#cliente.consultar__saldo()

#Depositando dinheiro
'''cliente.depositar(1000)
cliente.consultar__saldo()

#sleep(5)#Só para verificar a diferença de tempo entre as transações

cliente.consultar__limite_chequeespecial()

print("-" * 40)

cliente.historico__transacoes()

print("-" * 40)

cliente2 = ContaCorrente("Matheus", 11312313, 12313, 31313)

cliente.trasnferir(900, cliente2)

cliente.consultar__saldo()
cliente2.consultar__saldo()

cliente2.historico__transacoes()

#help(ContaCorrente)'''


'''cartao_cliente = CartaoCredito("João", cliente)#O usuário "Cliente" e todas as suas informações são passados como atributo da classe

print(cartao_cliente.conta_corrente._num_conta)#Usando as informação da conta criada pela classe ContaCorrente eu tenho o número

print(cartao_cliente.numero)

#print(cartao_cliente.cod_seguranca)

#print(cartao_cliente.validade)

print(cartao_cliente.senha)

cartao_cliente.senha = '1245'
print(cartao_cliente.senha)'''

#print(cliente.__dict__)#Enumera os valores da classe
#print(cartao_cliente.__dict__)

agencia_premium = AgenciaPremium(43242342, 43242423)

agencia_premium.adicionar_cliente("João", 31313, 543535)