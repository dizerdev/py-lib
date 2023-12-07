class Passaro:
    def __init__(self, vida, ataque, defesa):
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        self.alvo = alvo

    def fugir(self, destino):
        self.destino = destino


class PassaroAereo(Passaro):
    def voar(self, direcao):
        self.direcao = direcao


class PassaroAquatico(Passaro):
    def nadar(self, velocidade):
        self.velocidade = velocidade


class PassaroDeCompanhia(PassaroAereo):
    def __init__(self, vida, ataque, defesa, companheiro):
        self.companheiro = companheiro
        super().__init__(vida, ataque, defesa)


class Pinguin(PassaroAquatico):
    def __init__(self, vida, ataque, defesa, peso):
        self.peso = peso
        super().__init__(vida, ataque, defesa)


aguia = PassaroDeCompanhia(100, 300, 250, 'Diego')

pinguin = Pinguin(150, 80, 400, 5)

aguia.atacar('POO')
print(aguia.alvo)

pinguin.fugir('Norte')
print(pinguin.destino)

aguia.voar('Sul')
print(aguia.direcao)

pinguin.nadar('5km/h')
print(pinguin.velocidade)


print(aguia.vida, aguia.ataque, aguia.defesa, aguia.alvo, aguia.direcao)


print(f'{pinguin.vida} {pinguin.ataque} {pinguin.defesa} {pinguin.destino} {pinguin.velocidade}')
