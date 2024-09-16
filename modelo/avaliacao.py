class Avaliacao:
    avaliacoes = []

    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota
        self.avaliacoes.append(self)
    
    def __str__(self):
        return f"{self._cliente} | {self._nota}"