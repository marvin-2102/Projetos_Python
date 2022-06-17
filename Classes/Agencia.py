from random import randint

class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'Caixa atual abaixo do nível recomendado: R${self.caixa:,}, caixa indicado: R$1,000,000')
        else:
            print(f'Nível de caixa atual é de {self.caixa:,}')

    def emprestimo(self, valor, cpf, juros):
        if valor < self.caixa:
            self.emprestimos.append((valor, cpf, juros))
        else:
            pass

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


#Agência Virtual
class AgenciaVirtual(Agencia):#Passar "Agencia" no argumento, indica que é uma subclasse da classe geral "Agencia"

    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)#Aqui eu chamo o init da classe mâe "Agencia"
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor


#Agência Comum
class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=(1001, 9999))#Aqui eu chamo o init da classe mâe "Agencia"
        self.caixa = 1000000


#Agência Premium
class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=(1001, 9999))#Aqui eu chamo o init da classe mâe "Agencia"
        self.caixa = 50000000

    def adicionar_cliente(self, nome, cpf, patrimonio):#Mudando como o metódo adicionar cliente funciona nessa subclasse
        if patrimonio >= 1000000:
            print('Cliente cumpre os requisitos')
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print(f'Seu patrimonio precisa ser de pelo menos R$1,000,000, seu patrimonio atua é de R${patrimonio:,}')




if __name__ == '__main__':#Basicamente fala que esses códigos não vão ser usados se esse arquvio for exportado
    agencia_nv = Agencia(7879789, 9078097878, 8766986)#Agência qualquer

    agencia_virtual = AgenciaVirtual("AgenciaVirtual.com", 2313123, 3131313)    

    agencia_comum = AgenciaComum(3131331, 4234242)

    agencia_premium = AgenciaPremium(3424234, 454535)

    agencia_virtual.depositar_paypal(12000)

    agencia_virtual.verificar_caixa()

    agencia_premium.adicionar_cliente("João", 122112, 10000000)
    print(agencia_premium.clientes)




'''agencia_nv.caixa = 2000000

agencia_nv.verificar_caixa()

agencia_nv.emprestimo(3000, 453453, 0.05)

print(agencia_nv.emprestimos)

agencia_nv.adicionar_cliente("Marcus", 231231, 333344)

print(agencia_nv.clientes)'''
