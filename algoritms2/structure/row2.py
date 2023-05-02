class Row(object):
    def __init__(self):
        self.dados = []

    def insere(self, element):
        self.dados.append(element)

    def retira(self):
        return self.dados.pop(0)
            
    def vazia(self):
        return len(self.dados) == 0