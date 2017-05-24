class GameState(object):

    START = 1
    ESCOLHAS = 2
    PERSONAGEM = 3      #Personagem SELECTOR
    OPCOES = 4
    Controles = 5
    JOGO = 6
    GAME_OVER = 7

    def __init__(self,state = START):
        self.state = state

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state
