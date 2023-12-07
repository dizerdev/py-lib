from abc import ABC, abstractmethod


class Funcionario(ABC):
    @abstractmethod
    def salario(self):
        pass

    # fazendo uma property abstrata
    @property
    @abstractmethod
    def nome(self):
        return self._nome


class Vendedor(Funcionario):
    def salario(self):
        return super().salario()


class Estagiario(Funcionario):
    def salario(self):
        return 'Calculo 2'
