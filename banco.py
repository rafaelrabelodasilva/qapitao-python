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


fernando = ContaBancaria('Fernando', 1000)
ana = ContaBancaria('Ana', 2000)

fernando.consulta_saldo()
fernando.depositar(500)
fernando.consulta_saldo()
