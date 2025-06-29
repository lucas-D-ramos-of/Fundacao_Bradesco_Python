class Cliente:
    def __init__(self, n, t):
        self._nome = n
        self._telefone = t

    #Método get
    def get_nome(self):
        return self._nome

    #Método set
    def set_nome(self, nome):
        self._nome = nome