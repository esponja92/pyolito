import pygame


class ObjetoAtivo(pygame.Rect):

    def __init__(self, inicial_x, inicial_y, largura, altura, velocidade, cor):
        self.inicial_x = inicial_x
        self.inicial_y = inicial_y
        self.cor = cor

        self.largura = largura
        self.altura = altura
        self.velocidade = velocidade

        super(ObjetoAtivo, self).__init__(
            (self.inicial_x, self.inicial_y, self.largura, self.altura))

    def move_direita(self):
        self.x = self.x + self.velocidade

    def move_esquerda(self):
        self.x = self.x - self.velocidade

    def move_baixo(self):
        self.y = self.y + self.velocidade

    def move_cima(self):
        self.y = self.y - self.velocidade

    def colidiu_tela_direita(self, janela):
        return self.x >= (janela.get_width() - self.largura)

    def colidiu_tela_esquerda(self, janela):
        return self.x <= 0

    def colidiu_tela_cima(self, janela):
        return self.y <= 0

    def colidiu_tela_baixo(self, janela):
        return self.y >= (janela.get_height() - self.altura)

    def get_posicao_central_x(self):
        return self.x + self.largura/2

    def get_posicao_central_y(self):
        return self.y + self.altura/2

    def set_velocidade(self, velocidade):
        self.velocidade = velocidade

    def desenha(self, janela):
        pass

    def atualiza_posicao(self, listaObjetosAtivos, janela, keys):
        pass

    def reinicia(self):
        self.x = self.inicial_x
        self.y = self.inicial_y

    def _get_pixels_superficie(self):
        pixels = []

        for i in range(self.x, self.x+self.largura+1):
            for j in range(self.y, self.y+self.altura+1):
                pixels.append((i,j))

        return pixels

    # Pixel perfect
    def colidiu_com_objeto_ativo(self,objetoAtivo):
        pixels = self._get_pixels_superficie()
        pixelsObjetoAtivo = objetoAtivo._get_pixels_superficie()

        for x in pixels:
            if x in pixelsObjetoAtivo:
                return True

        return False
