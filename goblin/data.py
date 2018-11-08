from enum import IntEnum

class DataBase(object):
    @classmethod
    def get_data(cls, value, attribute = 'id'):
        for name, attr in vars(cls).items():
            if name[:1] == '_':
                continue
            if (value == attr[attribute]):
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

class Equipment_Set():
    LIGHT = [[1,1], [1,6], [2], [3], [1,1,1,1]]
    HEAVY = [[5, 6], [7, 8], [9, 9], [10], [5, 5, 11], [1,5, 11]]
    EXPLOSIVE = [[12, 8], [12, 12], [13, 13, 13], [14], [12, 13], [15]]
    MAGIC = [[16]]

class Ocupation(DataBase):
    MERCENARY = {'id': 1, 'name': 'Mercenário', 'attributes': (1,0,1,0), 'equip_set': Equipment_Set.HEAVY, 'skills': [1, 2, 3]}
    HUNTER = {'id': 2, 'name': 'Caçador', 'attributes': (1,0,0,1), 'equip_set': Equipment_Set.LIGHT, 'skills': [4, 5, 6]}
    THIEF = {'id': 3, 'name': 'Gatuno', 'attributes': (0,1,1,0), 'equip_set': Equipment_Set.LIGHT, 'skills': [7, 8, 9]}
    LEADER = {'id': 4, 'name': 'Lider', 'attributes': (1,1,0,0), 'equip_set': Equipment_Set.HEAVY, 'skills': [13, 2, 3]}
    PYRO = {'id': 5, 'name': 'Piromaníaco', 'attributes': (0,0,1,1), 'equip_set': Equipment_Set.EXPLOSIVE, 'skills': [10, 11, 12]}
    SHAMAN = {'id': 6, 'name': 'Xamã', 'attributes': (0,1,0,1), 'equip_set': Equipment_Set.MAGIC, 'skills': [14, 15, 16]}

class Skills(DataBase):
    MASTER_OF_WEAPONS = {'id': 1, 'name': 'Master of weapons', 'description': 'Você sempre rola+1 dado em todos os ataques que vocêfizer lutando com sua arma favorita (Escolha uma).'}
    BRUTAL_ATTACK = {'id': 2, 'name': 'Ataque Brutal', 'description': ' Uma vez ao dia vocêpode fazer um ataque brutal, que causao dobro de dano na vítima.'}
    FATAL_ATTACK = {'id': 3, 'name': 'Ataque Fatal', 'description': 'Uma vez ao dia você pode fazer um ataque fatal. Se acertar, a vitima deverá vencer um teste de Sorte (Dificuldade 5) ou morrerá imediatamente.'}
    TRACK = {'id': 4, 'name': 'Rastrear', 'description': 'Com um teste bem sucedido de Conhecimento (dificuldade 3) você pode rastrear qualquer criatura.'}
    SHARPSHOOTER = {'id': 5, 'name': 'Mira Certeira', 'description': ' Você ignora a proteçãodos seus oponentes.'}
    FATAL_SHOOT = {'id': 6, 'name': 'Tiro Fatal', 'description': 'Uma vez ao dia você podefazer um ataque à distância fatal. Se acertar, a vitima deverá vencer um teste de Sorte (Dificuldade 5) ou morrerá imediatamente.'}
    STEAL = {'id': 7, 'name': 'Roubar', 'description': 'Você pode roubar sem ser visto se vencer um teste resistido de Habilidade contra a vítima.'}
    SET_TRAP = {'id': 8, 'name': 'Armar Armadilhas', 'description': 'Você pode fazer uma armadilha em qualquer lugar se tiver alguns materiais. A pessoa terá que passar em um teste de Sorte (Dificuldade 5) para não cair na sua armadilha.'}
    STEALTH_ATTACK = {'id': 9, 'name': 'Ataque furtivo', 'description': 'Se você não foi visto, você pode fazer um ataque furtivo. Se acertar, a vitima deverá fazer um teste de Sorte (Dificuldade 5). Se ela falhar ela morrerá.'}
    ENDURANCE = {'id': 10, 'name': 'Resistencia', 'description': 'Você pode fazer um testede Sorte (dificuldade 5) quando receber dano de fogo ou explosão de fogo. Se vencer, você não recebe dano.'}
    EXPLOSIVE_SUICIDE = {'id': 11, 'name': 'Suícidio Explosivo', 'description': 'Usando sua arma, você pode se explodir e matar TODOS os que estiverem na área da explosão.'}
    IMMUNITY = {'id': 12, 'name': 'Imunidade', 'description': 'Você nunca recebe dano com fogo ou explosão.'}
    WARCRY = {'id': 13, 'name': 'Grito de Guerra', 'description': 'Uma vez ao dia você pode dar um grito que permitirá que todos seus aliados rolem 1 dado a mais para se esquivar até o final da batalha.'}
    MAGIC_MISSLE = {'id': 14, 'name': 'Tiro mágico', 'description': 'Você pode gastar pontos de magia para fazer ataques a distância. Cada ponto gasto causará um ponto de dano (pode gastar mais para fazer ataque com mais dano).'}
    HEAL = {'id': 15, 'name': 'Curar', 'description': 'Você pode gastar seus pontos de magia para curar seus aliados. Cada ponto de magia recupera um ponto de vitalidade.'}
    PETRIFY = {'id': 16, 'name': 'Petrificar', 'description': 'Gastando 6 pontos de magia você pode paralisar qualquer criatura.'}

class Equips(DataBase):
    DAGGER = {'id': 1, 'name': 'Adaga', 'damage': 2, 'protection': 0, 'throwable': True, 'distance': False}
    SIMPLE_BOW = {'id': 2, 'name': 'Arco Simples', 'damage': 2, 'protection': 0, 'throwable': False, 'distance': True}
    COMPOST_BOW = {'id': 3, 'name': 'Arco Composto', 'damage': 3, 'protection': 0, 'throwable': False, 'distance': True}
    CROSSBOW = {'id': 4, 'name': 'Besta', 'damage':3, 'protection': 0, 'throwable': True, 'distance': True}
    SWORD = {'id': 5, 'name': 'Espada', 'damage': 3, 'protection': 0, 'throwable': False, 'distance': False}
    SHIELD = {'id': 6, 'name': 'Escudo', 'damage': 0, 'protection': 1, 'throwable': False, 'distance': False}
    AXE = {'id': 7, 'name': 'Machado', 'damage': 4, 'protection': 0, 'throwable': False, 'distance': False}
    HELM = {'id': 8, 'name': 'Elmo', 'damage': 0, 'protection': 1, 'throwable': False, 'distance': False}
    THROW_AXE = {'id': 9, 'name': 'Machadinhas', 'damage': 3, 'protection': 0, 'throwable': True, 'distance': False}
    GREATSWORD = {'id': 10, 'name': 'Espadona', 'damage': 5, 'protection': 0, 'throwable': False, 'distance': False}
    ARMOR = {'id': 11, 'name': 'Armadura', 'damage': 0, 'protection': 1, 'throwable': False, 'distance': False}
    PISTOL = {'id': 12, 'name': 'Pistola', 'damage': 4, 'protection': 0, 'throwable': False, 'distance': True}
    EXPLOSIVE_CHICKEN = {'id': 13, 'name': 'Galinhas Explosivas', 'damage': 2, 'protection': 0, 'throwable': False, 'distance': False}
    POWDER_BARREL = {'id': 14, 'name': 'Barril de Pólvora', 'damage': 5, 'protection': 0, 'throwable': False, 'distance': False}
    CANNON = {'id': 15, 'name': 'Canhão', 'damage': 8, 'protection': 0, 'throwable': False, 'distance': True}
    CANNON = {'id': 16, 'name': 'Cajado', 'damage': 1, 'protection': 0, 'throwable': False, 'distance': True}

class Critic_Test(DataBase):
    EXPLODED = {'id': 1, 'name': 'Explode!'}
    LOST_HEAD = {'id': 2, 'name': 'Sem %s cabeça'}
    LOST_ARM = {'id': 3, 'name': 'Sem %s braço'}
    LOST_LEG = {'id': 4, 'name': 'Sem %s perna'}
    LOST_EYE = {'id': 5, 'name': 'Sem %s olho'}
    LOST_EAR = {'id': 6, 'name': 'Sem %s orelha'}
