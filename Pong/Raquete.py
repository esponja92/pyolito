import pygame

class Raquete(pygame.Rect):

    inicial_x = 0
    inicial_y = 0
    cor = ''

    LARGURA = 80
    ALTURA = 15
    VELOCIDADE = 5

    def __init__(self, centro_x, centro_y, cor):
        self.inicial_x = centro_x - self.LARGURA/2
        self.inicial_y = centro_y - self.ALTURA/2
        self.cor = cor
        super(Raquete, self).__init__((self.inicial_x, self.inicial_y, self.LARGURA, self.ALTURA))

    def move_direita(self):
        self.x = self.x + self.VELOCIDADE

    def move_esquerda(self):
        self.x = self.x - self.VELOCIDADE

    def pode_mover_direita(self, janela):
        return self.x < (janela.get_width() - self.LARGURA)

    def pode_mover_esquerda(self, janela):
        return self.x > 0

    def get_posicao_x(self):
        return self.x + self.LARGURA/2

    def get_posicao_y(self):
        return self.y + self.ALTURA/2

    def set_velocidade(self, velocidade):
        self.VELOCIDADE = velocidade

    def desenha(self, janela):
        pygame.draw.rect(janela, self.cor, self)