from modelo.cardapio.item_cardapio import Item_Cardapio

class Bebida(Item_Cardapio):
    
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)