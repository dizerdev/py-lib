class Mae:  # Mamifero
    def __init__(self, p1):
        print('executando o init da Mae')
        self.p1 = p1
        super().__init__()


class Filha(Mae):  # Felino
    def __init__(self, p1, p2):
        print('executando o init da Filha')
        self.p2 = p2
        super().__init__(p1)


class Neta(Filha):  # Gato
    def __init__(self, p1, p2, p3):
        self.p3 = p3
        print('executando o init da Neta')
        super().__init__(p1, p2)


class MeusDados(dict):
    def metodo_extra(self):
        pass


mae = Mae(1)
filha = Filha(1, 2)
neta = Neta(1, 2, 3)

isinstance(neta, Neta)  # True
isinstance(neta, Filha)  # True
isinstance(neta, Mae)  # True

isinstance(filha, Neta)  # False
isinstance(filha, Filha)  # True
isinstance(filha, Mae)  # True

isinstance(mae, Neta)  # False
isinstance(mae, Filha)  # False
isinstance(mae, Mae)  # True
