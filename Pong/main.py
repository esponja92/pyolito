import pygame
import sys
from pygame.locals import *
from Jogador import *
from Inimigo import *
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

        self.jogador = Jogador(self.JANELA_LARGURA/2,
                               self.JANELA_ALTURA - 15, pygame.Color('red'))

        self.inimigo = Inimigo(0, 15, pygame.Color('white'))
        self.inimigo.set_velocidade(4)

        self.bola = Bola(self.JANELA_LARGURA/2,
                         self.JANELA_ALTURA/2, 15, pygame.Color('white'))

        self.objetos = {'bola':self.bola,'jogador':self.jogador,'inimigo':self.inimigo}

        self.clock = pygame.time.Clock()

        pygame.display.set_caption('PyPong')
        pygame.init()

    def desenha(self):
        self.janela.fill(self.light_blue)

        for objeto in self.objetos:
            self.objetos[objeto].desenha(self.janela)

        pygame.display.update()

    def atualiza_posicao(self):
        keys = pygame.key.get_pressed()

        for objeto in self.objetos:
            self.objetos[objeto].atualiza_posicao(self.objetos, self.janela, keys)

    def gameLoop(self):
        self.desenha()

        while True:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_q)):
                    pygame.quit()
                    sys.exit()

            self.atualiza_posicao()

            self.desenha()


if __name__ == '__main__':
    game = Game()
    game.gameLoop()
