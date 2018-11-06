from goblin.data import *
import random

class Goblin(object):
    def __init__(self):
        self.level = 1
        self.skills = []
        self.weapons = []
        self.anomaly = []
        self.set_nome()
        self.color = Color().get_data(random.randint(1, 6))
        self.ocupation = Ocupation().get_data(random.randint(1, 6))
        self.features = Features().get_data(random.randint(1, 6))
        self.max_health = 4
        self.current_health = self.max_health

        for idx, skill in enumerate(self.ocupation['skills']):
            self.skills.append(Skills().get_data(skill))
        if self.features['id'] == 6:
            self.set_anomalies()

    @property
    def knowledge(self):
        return self.color['attributes'][0] + self.ocupacao['attributes'][0]
    @property
    def combat(self):
        return self.color['attributes'][1] + self.ocupacao['attributes'][1]
    @property
    def dexterity(self):
        return self.color['attributes'][2] + self.ocupacao['attributes'][2]
    @property
    def luck(self):
        return self.color['attributes'][3] + self.ocupacao['attributes'][3]

    def set_nome(self):
        self.nome = random.choice(['Sp', 'Cr', 'Bu', 'Ut', 'An', 'Om'])
        self.nome += random.choice(['or', 'ut', 'ar', 'an', 'ot', 'ec'])

    def set_anomalies(self):
        pass

    def set_health(self, value):
        self.current_health = max(0, min(value, self.max_health))

    def set_level(self, value):
        if value < 1:
            return
        self.level = value
        if self.level > 3:
            self.max_health = 4 + (self.level - 3)
