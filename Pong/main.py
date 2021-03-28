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

    GAME_OVER = False

    janela = ''
    clock = ''
    jogador = ''
    pontosJogador = 0
    inimigo = ''
    pontosInimigo = 0
    bola = ''
    objetos = []

    def __init__(self):
        self.janela = pygame.display.set_mode(
            (self.JANELA_LARGURA, self.JANELA_ALTURA))

        self.jogador = Jogador(self.JANELA_LARGURA/2,
                               self.JANELA_ALTURA - 15, pygame.Color('red'))

        self.inimigo = Inimigo(self.JANELA_LARGURA/2, 15, pygame.Color('white'))
        self.inimigo.set_velocidade(4)

        self.bola = Bola(self.JANELA_LARGURA/2,
                         self.JANELA_ALTURA/2, 15, pygame.Color('white'))

        self.objetos = {'bola':self.bola,'jogador':self.jogador,'inimigo':self.inimigo}

        self.clock = pygame.time.Clock()

        pygame.display.set_caption('PyPong')
        pygame.init()

        self.myfont = pygame.font.SysFont('Comic Sans MS', 48)

    def desenha(self):
        self.janela.fill(self.light_blue)

        self.atualiza_pontos()
        
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
        if(self.bola.colidiu_tela_cima(self.janela)):
            return True
        return False

    def jogadorPerdeu(self):
        if(self.bola.colidiu_tela_baixo(self.janela)):
            return True
        return False

    def atualiza_pontos(self):

        placar_jogador = self.myfont.render(str(self.pontosJogador), False, (0, 0, 0))
        self.janela.blit(placar_jogador,(self.JANELA_LARGURA/2,3*self.JANELA_ALTURA/4))

        placar_inimigo = self.myfont.render(str(self.pontosInimigo), False, (0, 0, 0))
        self.janela.blit(placar_inimigo,(self.JANELA_LARGURA/2,self.JANELA_ALTURA/4))

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
                self.pontosJogador = self.pontosJogador + 1
                self.reinicia()

            if(self.jogadorPerdeu()):
                self.pontosInimigo = self.pontosInimigo + 1
                self.reinicia()

            self.atualiza_posicao()
            self.desenha()


if __name__ == '__main__':
    game = Game()
    game.gameLoop()
