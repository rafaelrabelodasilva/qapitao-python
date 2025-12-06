class ContaBancaria:
    # Construtor: que é executado automaticamente quando eu ativar uma nova instancia
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        print(f'Depósito de R$ {valor} realizado com sucesso.')

    def consulta_saldo(self):
        print(f'Saldo atual de {self.titular}: R$ {self.saldo}')

class ContaCorrente(ContaBancaria):
    def sacar(self, valor):
        taxa = 2
        total = valor + taxa

        if(total > self.saldo):
            print('Saldo insuficiente para saque.')
        else:
          self.saldo = self.saldo - total
          print(f'Saque de R$ {valor} realizado com sucesso. Taxa de R$ {taxa} aplicada.')

class ContaPoupanca(ContaBancaria):
    def sacar(self, valor):
        if(valor > self.saldo):
            print('Saldo insuficiente para saque.')
        else:
          self.saldo = self.saldo - valor
          print(f'Saque de R$ {valor} realizado com sucesso.')


fernando = ContaCorrente('Fernando', 1000)
ana = ContaPoupanca('Ana', 2000)

fernando.sacar(500)
fernando.consulta_saldo()

ana.sacar(100)
ana.consulta_saldo()