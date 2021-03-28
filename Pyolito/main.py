import pygame
import sys
from pygame.locals import *
from ObjetoAtivo import *
from Constantes import *

class Game(object):

    FPS = 60

    JANELA_LARGURA = 640
    JANELA_ALTURA = 480

    GAME_OVER = False

    janela = ''
    clock = ''
    objetoAtivo1 = ''

    objetos = []

    def __init__(self):
        self.janela = pygame.display.set_mode(
            (self.JANELA_LARGURA, self.JANELA_ALTURA))

        # INICIALIZA OBJETOS DO JOGO
        self.objetoAtivo1 = ObjetoAtivo(0,0,0,0,0,0)
        self.objetos = {'objetoAtivo1':self.objetoAtivo1}

        self.clock = pygame.time.Clock()

        pygame.display.set_caption('TÍTULO DA JANELA')
        pygame.init()


    def desenha(self):
        self.janela.fill(COR_DE_FUNDO)

        for objeto in self.objetos:
            self.objetos[objeto].desenha(self.janela)

        pygame.display.update()

    def atualiza_posicao(self):
        keys = pygame.key.get_pressed()

        for objeto in self.objetos:
            self.objetos[objeto].atualiza_posicao(self.objetos, self.janela, keys)

    def reinicia(self):
        for objeto in self.objetos:
            self.objetos[objeto].reinicia()

    def jogadorGanhou(self):
        pass

    def jogadorPerdeu(self):
        pass

    def gameLoop(self):
        self.desenha()

        while not(self.GAME_OVER):
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_q)):
                    pygame.quit()
                    sys.exit()
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_r):
                    self.reinicia()

            if(self.jogadorGanhou()):
                pass

            if(self.jogadorPerdeu()):
                pass

            self.atualiza_posicao()
            self.desenha()


if __name__ == '__main__':
    game = Game()
    game.gameLoop()
