import pygame
from ObjetoAtivo import ObjetoAtivo


class Raquete(ObjetoAtivo):

    def __init__(self, centro_x, centro_y, cor):
        self.largura = 80
        self.altura = 15
        self.velocidade = 5

        self.inicial_x = centro_x - self.largura/2
        self.inicial_y = centro_y - self.altura/2
        self.cor = cor

        super().__init__(self.inicial_x, self.inicial_y,
                         self.largura, self.altura, self.velocidade, self.cor)

    def desenha(self, janela):
        pygame.draw.rect(janela, self.cor, self)
