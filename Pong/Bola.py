import pygame
from ObjetoAtivo import ObjetoAtivo

class Bola(ObjetoAtivo):

    def __init__(self, centro_x, centro_y, raio, cor):
        self.LARGURA = 15
        self.ALTURA = 15
        self.VELOCIDADE = 2

        self.inicial_x = centro_x
        self.inicial_y = centro_y
        self.cor = cor

        self.raio = raio

        super().__init__(self.inicial_x, self.inicial_y, self.LARGURA, self.ALTURA, self.VELOCIDADE, self.cor)

    def desenha(self, janela):
        pygame.draw.circle(janela, self.cor, (self.x, self.y), self.raio)