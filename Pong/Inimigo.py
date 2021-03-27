import pygame
from Raquete import Raquete

class Inimigo(Raquete):

    LARGURA = ''
    ALTURA = ''
    VELOCIDADE = ''

    inicial_x = ''
    inicial_y = ''
    cor = ''

    def __init__(self, centro_x, centro_y, cor):
        super().__init__(centro_x, centro_y, cor)

    def atualiza_posicao(self, listaObjetosAtivos, janela, keys):
        if(listaObjetosAtivos['bola'].get_posicao_central_x() > self.get_posicao_central_x() and self.pode_mover_direita(janela)):
            self.move_direita()

        if(listaObjetosAtivos['bola'].get_posicao_central_x() < self.get_posicao_central_x() and self.pode_mover_esquerda(janela)):
            self.move_esquerda()