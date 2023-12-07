class ContaBancaria:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.__saldo = 0

    @property
    def saldo(self):
        return self.__saldo

    def ver_saldo(self):
        return f'Seu saldo é R${self.__saldo}'

    def depositar(self, valor):
        if valor < 0:
            return 'Valor deve ser positivo'
        self.__saldo += valor
        return 'Deposito realizado com sucesso'

    def sacar(self, valor):
        if valor > self.__saldo:
            return 'Saldo insuficiente'
        elif valor == 0 or valor < 0:
            return 'Valor invalido'
        self.__saldo -= valor
        return 'Saque realizado com sucesso'


class ContaInvestimento(ContaBancaria):
    def __init__(self, numero, titular, gerente):
        self.gerente = gerente
        super().__init__(numero, titular)


class ContaPoupanca(ContaBancaria):
    def __init__(self, numero, titular):
        self.rendimento = 0.5
        super().__init__(numero, titular)

    def sacar(self, valor):
        if valor > self.saldo:
            print('deposite')
        return super().sacar(valor)


cp1 = ContaInvestimento(1, 'Diego', 'Impacta')
cp2 = ContaPoupanca(2, 'Lucia')

cp1.depositar(500)
cp2.depositar(400)

cp1.sacar(200)

print(cp1.saldo)