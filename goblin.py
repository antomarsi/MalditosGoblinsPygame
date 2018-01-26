from enum import Enum
import json, random
from pprint import pprint

class Equipamento():
    code = 10
    nome = "Nenhum"
    dano = 0
    protecao = 0
    distancia = False
    arremesar = False
    qtd = 0

    def __init__(self, arma):

        self.code = arma["code"]
        self.nome = arma["nome"]
        self.dano = arma["dano"]
        self.protecao = arma["protecao"]
        self.distancia = arma["distancia"]
        self.arremesar = arma["arremesar"]

    def set_qtd(self, qtd):
        self.qtd = qtd

    def __str__(self):
        return '{}-{} ({},{},{},{})'.format(
            str(self.code), self.nome, str(self.dano),
            str(self.protecao), str(self.distancia), str(self.arremesar))

class Database():
    coloracao = []
    ocupacao = []
    carac = []
    sets = []
    armas = []

class Goblin():
    combate = 0
    conhecimento = 0
    habilidade = 0
    sorte = 0
    equipamento = []
    vitalidade = 4
    anomalia = []
    db = Database()

    changed = True

    def __init__(self, json_file):
        json_decoded = json.load(open(json_file))
        self.db.coloracao = json_decoded['Coloracao']
        self.db.ocupacao = json_decoded['Ocupacao']
        self.db.carac = json_decoded['Caracteristica']
        self.db.sets = json_decoded['Sets']
        self.db.armas = json_decoded['Armas']
        #print(self.database)
        self.criarGoblin()

    def criarGoblin(self):

        self.cor = self.db.coloracao[random.randint(1, len(self.db.coloracao))-1]
        self.ocupacao = self.db.ocupacao[random.randint(1, len(self.db.ocupacao))-1]
        self.caracteristica = self.db.carac[random.randint(1, len(self.db.carac))-1]

        self.combate = self.ocupacao['bonus'][0]
        self.conhecimento = self.ocupacao['bonus'][1]
        self.habilidade = self.ocupacao['bonus'][2]
        self.sorte = self.ocupacao['bonus'][3]
        self.tipo  = self.ocupacao['tipo']
        for equip_set in self.db.sets:
            if equip_set['code'] == self.tipo:
                for weapon in equip_set['sets'][random.randint(1, len(equip_set['sets']))-1]:
                    for i in range(weapon['qtd']):
                        self.equipamento.append(Equipamento(self.db.armas[weapon['code']-1]))
        self.nivel = 1
        self.nome = random.choice(['Sp', 'Cr', 'Bu', 'Ut', 'An', 'Om'])
        self.nome += random.choice(['or', 'ut', 'ar', 'an', 'ot', 'ec'])
        if self.caracteristica == self.db.carac[5]:
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
        protecao = 0
        for eqp in self.equipamento:
            protecao += eqp.protecao
        return protecao

    def get_changed(self):
        return self.changed
