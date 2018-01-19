from enum import Enum
import random

class Coloracao(Enum):
    VERDE_CLARO = 1
    VERDE = 2
    VERDE_ESCURO = 3
    AMARELO = 4
    VERMELHO = 5
    AZUL = 6

class Ocupacao(Enum):

    MERCENARIO = 1
    CACADOR = 2
    GATUNO = 3
    LIDER = 4
    PIROMANIACO = 5
    XAMA = 6

class Caracteristica(Enum):
    INSANO = 1
    FEDORENTO = 2
    CICATRIZES = 3
    GORDO = 4
    FALA_ERRADO = 5
    ANOMALIA = 6

class Goblin():
    combate = 0
    conhecimento = 0
    habilidade = 0
    sorte = 0
    equipamento = []
    vitalidade = 4
    anomalia = []

    def __init__(self):
        self.cor = random.randint(1, 6)
        self.ocupacao = random.randint(1, 6)
        self.caracteristica = random.randint(1, 6)
        self.nivel = 1
        self.nome = random.choice(['Sp', 'Cr', 'Bu', 'Ut', 'An', 'Om'])
        self.nome += random.choice(['or', 'ut', 'ar', 'an', 'ot', 'ec'])
        self.set_anomalia()

    def set_anomalia(self):
        dado = random.randint(2,12)
        if dado == 2 or dado == 3:
            self.anomalia.append("Manchas rosas")
        if dado == 4:
            self.anomalia.append("Orelhas no sovaco")
        if dado == 5:
            self.anomalia.append("Corcunda")
        if dado == 6:
            self.anomalia.append("Braço extra atrofiado")
        if dado == 7:
            self.anomalia.append(str(random.randint(1,6))+" Olhos")
        if dado == 8:
            self.anomalia.append("Olhos Gigantes")
        if dado == 9:
            self.anomalia.append("Mãos Gigantes")
        if dado == 10:
            self.anomalia.append("Duas Cabeças")
        if dado == 11 or dado == 12:
            self.set_anomalia()
            self.set_anomalia()

    def get_dano(self):
        pass

    def get_protecao(self):
        pass

    def get_text_carac(self):
        if self.caracteristica == Caracteristica.INSANO:
            return "Insano"
        if self.caracteristica == Caracteristica.FEDORENTO:
            return "Fedorento"
        if self.caracteristica == Caracteristica.CICATRIZES:
            return "Cicatrizes"
        if self.caracteristica == Caracteristica.GORDO:
            return "Gordo"
        if self.caracteristica == Caracteristica.FALA_ERRADO:
            return "Fala errado"
        if self.caracteristica == Caracteristica.ANOMALIA:
            return "Anomalia ("+(', '.join(self.anomalia)+")"
