import pygame
from ObjetoAtivo import ObjetoAtivo

class Raquete(ObjetoAtivo):
    
    def __init__(self, centro_x, centro_y, cor):
        self.LARGURA = 80
        self.ALTURA = 15
        self.VELOCIDADE = 5

        self.inicial_x = centro_x - self.LARGURA/2
        self.inicial_y = centro_y - self.ALTURA/2
        self.cor = cor

        super().__init__(self.inicial_x, self.inicial_y, self.LARGURA, self.ALTURA, self.VELOCIDADE, self.cor)

    def desenha(self, janela):
        pygame.draw.rect(janela, self.cor, self)