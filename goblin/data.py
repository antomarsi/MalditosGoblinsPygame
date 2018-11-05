from enum import Enum

class DataBase(object):
    @classmethod
    def get_data(cls, value):
        for name, attr in vars(cls).items():
            if name[:1] == '_':
                continue
            if (value == attr['id']):
                return attr
        raise Exception('Data not found')

class Color(DataBase):
    LIGHT_GREEN = {'id': 1, 'name': 'Verde Claro', 'attributes': (2,2,1,1)}
    GREEN = {'id': 2, 'name': 'Verde', 'attributes': (2,2,1,1)}
    DARK_GREEN = {'id': 3, 'name': 'Verde Escuro', 'attributes': (1,2,2,1)}
    YELLOW = {'id': 4, 'name': 'Amarelo', 'attributes': (2,1,1,2)}
    RED = {'id': 5, 'name': 'Vermelho', 'attributes': (1,1,2,2)}
    BLUE = {'id': 6, 'name': 'Azul', 'attributes': (1,2,1,2)}

class Features(DataBase):
    INSANE = {'id': 1, 'name': 'Insano', 'description': 'Você não tem controle de seus atos. Sempre que o mestre quiser, ele pode pedir um teste de Sorte (dificuldade 5). Se você falhar, o mestre poderá decidir um ato idiota para seu personagem fazer'}
    STINKY = {'id': 2, 'name': 'Fedorento', 'description': 'Você fede e ninguém gosta de ficar perto. Qualquer um que fique por mais de 1 minuto perto de você, poderá ficar nauseado e vomitar.'}
    SCARS = {'id': 3, 'name': 'Cicatrizes', 'description': 'Você possui muitas cicatrizes de muitas batalhas. As fêmeas goblins nunca olharão para você.'}
    FAT = {'id': 4, 'name': 'Gordo', 'description': 'Você é obeso e tem problemas em passar em buracos estreitos, se esconder e não consegue correr por muito tempo.'}
    SPEAK_WRONG = {'id': 5, 'name': 'Fala errado', 'description': 'Você tem algum problema de comunicação (gagueira, língua presa, troca letras, etc) e isso irrita muito os seus companheiros.'}
    ANOMALY = {'id': 6, 'name': 'Anomalia', 'description': 'Você possui uma anomalia genética'}

class Anomalies(DataBase):
    PINK_SPOTS = {'id': 3, 'name': 'Manchas rosas'}
    EAR_IN_ARMPIT = {'id': 4, 'name': 'Orelhas no sovaco'}
    HUMP = {'id': 5, 'name': 'Corcunda'}
    EXTRA_ARM = {'id': 6, 'name': 'Braço extra atrofiado'}
    N_EYES = {'id': 7, 'name': '%d Olho(s)'}
    GIANT_EYES = {'id': 8, 'name': 'Olhos Gigantes'}
    GIANT_HANDS = {'id': 9, 'name': 'Mãos Gigantes'}
    TWO_HEADS = {'id': 10, 'name': 'Duas Cabeças'}

class Ocupation(DataBase):
    MERCENARY = {'id': 1, 'name': 'Mercenário', 'attributes': (1,0,1,0), 'equip_type': 2, 'skills': [1, 2, 3]}
    HUNTER = {'id': 2, 'name': 'Caçador', 'attributes': (1,0,0,1), 'equip_type': 1, 'skills': [4, 5, 6]}
    THIEF = {'id': 3, 'name': 'Gatuno', 'attributes': (0,1,1,0), 'equip_type': 1, 'skills': [7, 8, 9]}
    LEADER = {'id': 4, 'name': 'Lider', 'attributes': (1,1,0,0), 'equip_type': 2, 'skills': [13, 2, 3]}
    PYRO = {'id': 5, 'name': 'Piromaníaco', 'attributes': (0,0,1,1), 'equip_type': 3, 'skills': [10, 11, 12]}
    SHAMAN = {'id': 6, 'name': 'Xamã', 'attributes': (0,1,0,1), 'equip_type': 1, 'skills': [14, 15, 16]}

class Equipment_Type(Enum):
    LIGHT = 1
    HEAVY = 2
    EXPLOSIVE = 3
    MAGIC = 3

class Skills(DataBase):
    MASTER_OF_WEAPONS = {'id': 1, 'name': 'Master of weapons', 'description': 'teste'}
    BRUTAL_ATTACK = {'id': 2, 'name': 'Ataque Brutal', 'description': 'teste'}
    FATAL_ATTACK = {'id': 3, 'name': 'Ataque Fatal', 'description': 'teste'}
    TRACK = {'id': 4, 'name': 'Rastrear', 'description': 'teste'}
    SHARPSHOOTER = {'id': 5, 'name': 'Tiro Certeiro', 'description': 'teste'}
    FATAL_SHOOT = {'id': 6, 'name': 'Tiro Fatal', 'description': 'teste'}
    STEAL = {'id': 7, 'name': 'Roubar', 'description': 'teste'}
    SET_TRAP = {'id': 8, 'name': 'Armadilha', 'description': 'teste'}
    STEALTH_ATTACK = {'id': 9, 'name': 'Ataque furtivo', 'description': 'teste'}
    ENDURANCE = {'id': 10, 'name': 'Resistencia', 'description': 'teste'}
    EXPLOSIVE_SUICIDE = {'id': 11, 'name': 'Suícidio Explosivo', 'description': 'teste'}
    IMMUNITY = {'id': 12, 'name': 'Imunidade', 'description': 'teste'}
    WARCRY = {'id': 13, 'name': 'Grito de Guerra', 'description': 'teste'}
    MAGIC_MISSLE = {'id': 14, 'name': 'Tiro mágico', 'description': 'teste'}
    HEAL = {'id': 15, 'name': 'Curar', 'description': 'teste'}
    PETRIFY = {'id': 16, 'name': 'Petrificar', 'description': 'teste'}

class Weapons(DataBase):
    DAGGER = {'id': 1, 'name': 'Adaga', 'damage': 2, 'protection': 0, 'throwable': True, 'distance': False}
    SIMPLE_BOW = {'id': 1, 'name': 'Arco Simples', 'damage': 2, 'protection': 0, 'throwable': False, 'distance': True}
    COMPOST_BOW = {'id': 1, 'name': 'Arco Composto', 'damage': 3, 'protection': 0, 'throwable': False, 'distance': True}
    CROSSBOW = {'id': 1, 'name': 'Besta', 'damage':3, 'protection': 0, 'throwable': True, 'distance': True}
    SWORD = {'id': 1, 'name': 'Espada', 'damage': 3, 'protection': 0, 'throwable': False, 'distance': False}
    SHIELD = {'id': 1, 'name': 'Escudo', 'damage': 0, 'protection': 1, 'throwable': False, 'distance': False}
    AXE = {'id': 1, 'name': 'Machado', 'damage': 4, 'protection': 0, 'throwable': False, 'distance': False}
    HELM = {'id': 1, 'name': 'Elmo', 'damage': 0, 'protection': 1, 'throwable': False, 'distance': False}
    THROW_AXE = {'id': 1, 'name': 'Machadinhas', 'damage': 3, 'protection': 0, 'throwable': True, 'distance': False}
    GREATSWORD = {'id': 1, 'name': 'Espadona', 'damage': 5, 'protection': 0, 'throwable': False, 'distance': False}
    ARMOR = {'id': 1, 'name': 'Armadura', 'damage': 0, 'protection': 1, 'throwable': False, 'distance': False}
    PISTOL = {'id': 1, 'name': 'Pistola', 'damage': 4, 'protection': 0, 'throwable': False, 'distance': True}
    EXPLOSIVE_CHICKEN = {'id': 1, 'name': 'Galinhas Explosivas', 'damage': 2, 'protection': 0, 'throwable': False, 'distance': False}
    POWDER_BARREL = {'id': 1, 'name': 'Barril de Pólvora', 'damage': 5, 'protection': 0, 'throwable': False, 'distance': False}
    CANNON = {'id': 1, 'name': 'Canhão', 'damage': 8, 'protection': 0, 'throwable': False, 'distance': True}

class Critic_Test(DataBase):
    EXPLODED = {'id': 1, 'name': 'Explode!'}
    LOST_HEAD = {'id': 2, 'name': 'Sem %s cabeça'}
    LOST_ARM = {'id': 3, 'name': 'Sem %s braço'}
    LOST_LEG = {'id': 4, 'name': 'Sem %s perna'}
    LOST_EYE = {'id': 5, 'name': 'Sem %s olho'}
    LOST_EAR = {'id': 6, 'name': 'Sem %s orelha'}
