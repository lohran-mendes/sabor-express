from abc import ABC, abstractmethod

class Item_Cardapio(ABC):

    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
        
    @abstractmethod
    def aplicar_desconto(self):
        pass
