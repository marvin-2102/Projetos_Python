from datetime import datetime
import pytz
from sympy import NumberSymbol
from random import randint


class ContaCorrente:#Separe as palavras nas classes com letra maiuscúla

    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes.

    Atributos:
        nome: Nome do cliente
        cpf: CPF do cliente
        agencia: Número da agência do cliente
        num_conta: Número da conta do cliente
        saldo: Dinheiro na conta do cliente
        limite: Limite do cheque especial do cliente
        transacoes: Histórico de transações do cliente
    """

    @staticmethod
    def _data_hora():#FUNÇÃO QUE NÃO MUDA
        fuso_brasil = pytz.timezone('Brazil/East')#Define para o fuso-horário de Brasília
        horario_transacao_brasil = datetime.now(fuso_brasil)
        return horario_transacao_brasil.strftime("%d/%m/%Y %H:%M:%S")

    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None#Inicializando o atributo _limite
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self.cartoes = []#Início uma lista para guardar os cartões da conta

    def consultar__saldo(self):
        print(f'Seu saldo é de R${self._saldo:,.2f}')

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, f"Saldo: {self._saldo}", ContaCorrente._data_hora()))

    def __limite_conta(self):#O "underline antes do metódo indica que ele só vai ser usado dentro da classe"
        self._limite = -100
        return self._limite

    def sacar(self, valor):
        if self._saldo - valor < self.__limite_conta():#O crédito especial _limite é de R$100(Cheque especial)
            print("Não será possível retirar esse valor poís ele excede o _limite de crédito da conta")
            sacar_maximo = input("Gostaria de retirar o valor máximo? [S/N]").upper()
            if sacar_maximo == "S":
                self._saldo -= (self._saldo + 100)#O valor máximo a ser retirado é de R$100 além do disponível na conta
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, f"Saldo: {self._saldo}", ContaCorrente._data_hora()))
            
    def consultar__limite_chequeespecial(self):
        print(f'Seu _limite de cheque especial é de R${self.__limite_conta() * -1:,.2f}')

    def historico__transacoes(self):
        print("Histórico de transações: ")
        print("Movimentação na conta | Saldo da conta | Data e hora da transação")
        for transacao in self._transacoes:
            print(transacao)

    def trasnferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, f"Saldo: {self._saldo}", ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, f"Saldo: {self._saldo}", ContaCorrente._data_hora()))


class CartaoCredito:

    @staticmethod
    def _data_hora():#FUNÇÃO QUE NÃO MUDA
        fuso_brasil = pytz.timezone('Brazil/East')#Define para o fuso-horário de Brasília
        horario_transacao_brasil = datetime.now(fuso_brasil)
        return horario_transacao_brasil

    def __init__(self, titular, conta_corrente):
        self.numero = f'{randint(1000, 9999)} {randint(1000, 9999)} {randint(1000, 9999)} {randint(1000, 9999)}'
        self.titular = titular
        self.validade = f"{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 8}"
        self.cod_seguranca = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
        self.limite = 1500
        self._senha = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)#Fazendo uma correlação entre as duas classes

    @property#Torna o metódo "senha" um atributo
    def senha(self):
        return self._senha
        
    @senha.setter 
    def senha(self, valor):#Verificar se uma nova senha é válida
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
