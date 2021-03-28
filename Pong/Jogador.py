import pygame
from Raquete import Raquete


class Jogador(Raquete):

    LARGURA = ''
    ALTURA = ''
    VELOCIDADE = ''

    inicial_x = ''
    inicial_y = ''
    cor = ''

    def __init__(self, centro_x, centro_y, cor):
        super().__init__(centro_x, centro_y, cor)

    def atualiza_posicao(self, listaObjetosAtivos, janela, keys):
        if(keys[pygame.K_RIGHT] and not(self.colidiu_tela_direita(janela))):
            self.move_direita()

        if(keys[pygame.K_LEFT] and not(self.colidiu_tela_esquerda(janela))):
            self.move_esquerda()
