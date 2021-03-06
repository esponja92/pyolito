import pygame
from ObjetoAtivo import ObjetoAtivo


class Bola(ObjetoAtivo):

    def __init__(self, centro_x, centro_y, raio, cor):
        self.largura = 15
        self.altura = 15
        self.velocidade = 5

        self.inicial_x = centro_x
        self.inicial_y = centro_y
        self.cor = cor

        self.raio = raio

        self.direcao_vertical = 1
        self.direcao_horizontal = 0

        super().__init__(self.inicial_x, self.inicial_y,
                         self.largura, self.altura, self.velocidade, self.cor)

    def desenha(self, janela):
        pygame.draw.circle(janela, self.cor, (self.x, self.y), self.raio)

    def reinicia(self):
        super().reinicia()
        self.direcao_vertical = 1
        self.direcao_horizontal = 0

    def atualiza_posicao(self, listaObjetosAtivos, janela, keys):
        if(self.colliderect(listaObjetosAtivos['jogador'])):
            self.direcao_vertical = -1

            if(abs(self.get_posicao_central_x() - listaObjetosAtivos['jogador'].get_posicao_central_x()) <= 7.5):
                self.direcao_horizontal = 0

            elif(self.get_posicao_central_x() > listaObjetosAtivos['jogador'].get_posicao_central_x()):
                self.direcao_horizontal = 1
            
            elif(self.get_posicao_central_x() < listaObjetosAtivos['jogador'].get_posicao_central_x()):
                self.direcao_horizontal = -1

        elif(self.colliderect(listaObjetosAtivos['inimigo'])):
            self.direcao_vertical = 1

        if(self.colidiu_tela_direita(janela)):
            self.direcao_horizontal = -1

        if(self.colidiu_tela_esquerda(janela)):
            self.direcao_horizontal = 1

        #atualiza a posicao da bola
        if(self.direcao_vertical == -1):
            self.move_cima()
        
        if(self.direcao_vertical == 1):
            self.move_baixo()

        if(self.direcao_horizontal == 1):
            self.move_direita()
        
        if(self.direcao_horizontal == -1):
            self.move_esquerda()
        

