# Problema 1: pontos de ação tão ficando negativos

from abc import ABC, abstractmethod


class Soldados(ABC):

    @abstractmethod
    def __init__(self, nome, fortaleza):
        self.pontos_acao = 10
        self.arma_fogo = False
        self.inventario = []

        self.nome = nome
        self.fortaleza = fortaleza

    @abstractmethod
    def avancar(self, qtd_casas: int):
        if self.pontos_acao - qtd_casas >= 0:
            print(f"{self.nome} está avançando {qtd_casas} casas")
            self.pontos_acao -= qtd_casas
        else:
            print(f"{self.nome} não pode mais agir")

    @abstractmethod
    def atirar(self):
        if self.pontos_acao - 4 >= 0:
            if self.arma_fogo:
                print(f"{self.nome} atirou!")
                self.pontos_acao -= 4
            else:
                print(f"{self.nome} não possui uma arma")
        else:
            print(f"{self.nome} não pode mais agir")

    @abstractmethod
    def defender(self):
        if self.pontos_acao - 3 >= 0:
            print(f"{self.nome} defendeu")
            self.pontos_acao -= 3
        else:
            print(f"{self.nome} não pode mais agir")

    @abstractmethod
    def atacar(self):
        if self.pontos_acao - 5 >= 0:
            print(f"{self.nome} está atacando")
            self.pontos_acao -= 5
        else:
            print(f"{self.nome} não pode mais agir")


class Cavaleiros(Soldados):
    def __init__(self, nome, fortaleza):
        super().__init__(nome, fortaleza)
        self.inventario = ["Espada", "Escudo"]

    def atacar(self):
        super().atacar()

    def atirar(self):
        super().atirar()

    def avancar(self, qtd_casas):
        super().avancar(qtd_casas)

    def defender(self):
        super().defender()

    def atacar_com(self, equipamento):
        if self.pontos_acao - 6 >= 0:
            print(f"{self.nome} está atacando com {equipamento}")
            self.pontos_acao -= 6
        else:
            print(f"{self.nome} não pode mais agir")


reginaldo = Cavaleiros("Reginaldo", "Templarios")

reginaldo.defender()
reginaldo.defender()
reginaldo.avancar(5)
print(reginaldo.pontos_acao)
