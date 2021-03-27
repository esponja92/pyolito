import pygame
import sys
from pygame.locals import *
from Raquete import *
from Bola import *


class Game(object):

    # constantes
    light_blue = [51, 204, 255]

    FPS = 60

    JANELA_LARGURA = 640
    JANELA_ALTURA = 480

    janela = ''
    clock = ''
    jogador = ''
    inimigo = ''
    bola = ''
    objetos = []

    def __init__(self):
        self.janela = pygame.display.set_mode(
            (self.JANELA_LARGURA, self.JANELA_ALTURA))

        self.jogador = Raquete(self.JANELA_LARGURA/2,
                               self.JANELA_ALTURA - 15, pygame.Color('red'))

        self.inimigo = Raquete(0, 15, pygame.Color('white'))
        self.inimigo.set_velocidade(3)

        self.bola = Bola(self.JANELA_LARGURA/2,
                         self.JANELA_ALTURA/2, 15, pygame.Color('white'))

        self.objetos = [self.jogador, self.inimigo, self.bola]

        self.clock = pygame.time.Clock()

        pygame.display.set_caption('PyPong')
        pygame.init()

    def atualiza_jogo(self):
        self.janela.fill(self.light_blue)

        for objeto in self.objetos:
            objeto.desenha(self.janela)

        pygame.display.update()

    def move_jogador(self, keys):
        if(keys[pygame.K_RIGHT] and self.jogador.pode_mover_direita(self.janela)):
            self.jogador.move_direita()

        if(keys[pygame.K_LEFT] and self.jogador.pode_mover_esquerda(self.janela)):
            self.jogador.move_esquerda()

    def move_inimigo(self, bola):
        if(bola.get_posicao_x() > self.inimigo.get_posicao_x() and self.inimigo.pode_mover_direita(self.janela)):
            self.inimigo.move_direita()

        if(bola.get_posicao_x() < self.inimigo.get_posicao_x() and self.inimigo.pode_mover_esquerda(self.janela)):
            self.inimigo.move_esquerda()

    def gameLoop(self):
        self.atualiza_jogo()

        while True:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_q)):
                    pygame.quit()
                    sys.exit()

            # move jogador
            keys = pygame.key.get_pressed()
            self.move_jogador(keys)

            # move bola

            # move inimigo
            self.move_inimigo(self.bola)

            self.atualiza_jogo()


if __name__ == '__main__':
    game = Game()
    game.gameLoop()
