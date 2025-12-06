class ContaBancaria:
    # Construtor: que é executado automaticamente quando eu ativar uma nova instância
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


fernando = ContaBancaria('Fernando', 1000)
ana = ContaBancaria('Ana', 2000)

print(fernando.titular)