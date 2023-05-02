class Pile(object):
    def __init__(self):
        self.dados = []

    def push(self, element):
        self.dados.append(element)
    
    def pop(self):
        if not self.vazia():
            return self.dados.pop(-1)

    def empty(self):
        return len(self.dados) == 0

    