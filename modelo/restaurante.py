import os

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self.categoria} | {self.ativo}'

    @classmethod  
    def listar_restaurantes(cls):
        print(f'\n{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'.ljust(20)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.ativo}')
        print()

    @property
    def ativo(self):
        return 'ativo' if self._ativo else 'desativado'
    
    def alterar_estado(self):
        self._ativo = not self._ativo
