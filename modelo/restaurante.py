import os
from modelo.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []


    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._avaliacoes} |  {self._ativo}'

    @classmethod  
    def listar_restaurantes(cls):
        print(f'\n{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'.ljust(20)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo}')
        print()

    @property
    def ativo(self):
        return 'ativo' if self._ativo else 'desativado'
    
    def alterar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 <= nota <= 5: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return '-'
        soma_avaliacao = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade_avaliacao = len(self._avaliacoes)
        media = round((soma_avaliacao / quantidade_avaliacao), 1)
        return media
