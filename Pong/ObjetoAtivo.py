import pygame


class ObjetoAtivo(pygame.Rect):

    def __init__(self, inicial_x, inicial_y, LARGURA, ALTURA, VELOCIDADE, cor):
        self.inicial_x = inicial_x
        self.inicial_y = inicial_y
        self.cor = cor

        self.LARGURA = LARGURA
        self.ALTURA = ALTURA
        self.VELOCIDADE = VELOCIDADE

        super(ObjetoAtivo, self).__init__(
            (self.inicial_x, self.inicial_y, self.LARGURA, self.ALTURA))

    def move_direita(self):
        self.x = self.x + self.VELOCIDADE

    def move_esquerda(self):
        self.x = self.x - self.VELOCIDADE

    def move_baixo(self):
        self.y = self.y + self.VELOCIDADE

    def move_cima(self):
        self.y = self.y - self.VELOCIDADE

    def pode_mover_direita(self, janela):
        return self.x < (janela.get_width() - self.LARGURA)

    def pode_mover_esquerda(self, janela):
        return self.x > 0

    def get_posicao_central_x(self):
        return self.x + self.LARGURA/2

    def get_posicao_central_y(self):
        return self.y + self.ALTURA/2

    def set_velocidade(self, velocidade):
        self.VELOCIDADE = velocidade

    def desenha(self, janela):
        pass

    def atualiza_posicao(self, listaObjetosAtivos, janela, keys):
        pass

    def reinicia(self):
        self.x = self.inicial_x
        self.y = self.inicial_y
