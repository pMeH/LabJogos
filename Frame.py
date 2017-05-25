class Frame(object):

    JOGAR = 1
    CONTROLES = 2
    SAIR = 3
    def __init__(self,state = JOGAR):
        self.state = state

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state
