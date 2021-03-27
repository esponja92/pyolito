import pygame

class Bola(pygame.Rect):

    inicial_x = 0
    inicial_y = 0
    cor = ''

    LARGURA = 15
    ALTURA = 15
    VELOCIDADE = 2

    def __init__(self, centro_x, centro_y, raio, cor):
        self.inicial_x = centro_x
        self.inicial_y = centro_y
        self.cor = cor
        super(Bola, self).__init__((self.inicial_x, self.inicial_y, self.LARGURA, self.ALTURA))
        self.raio = raio

    def move_direita(self):
        self.x = self.x + self.VELOCIDADE

    def move_esquerda(self):
        self.x = self.x - self.VELOCIDADE

    def pode_mover_direita(self, janela):
        return self.x < (janela.get_width() - self.LARGURA)

    def pode_mover_esquerda(self, janela):
        return self.x > 0

    def get_posicao_x(self):
        return self.x

    def get_posicao_y(self):
        return self.y

    def set_velocidade(self, velocidade):
        self.VELOCIDADE = velocidade

    def desenha(self, janela):
        pygame.draw.circle(janela, self.cor, (self.x, self.y), self.raio)