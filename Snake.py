import pygame
from pygame.locals import *

pygame.init()

#tela
tamanho_tela = (600, 600)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption('Jogo da Cobrinha')

#Direções cobrinha
left = K_LEFT
right = K_RIGHT      
up = K_UP
down = K_DOWN

passo = 10

#cobrinha
cobrinha_pos = [(300, 300)]
cobrinha_sup = pygame.Surface((10, 10))
cobrinha_sup.fill((0,255,0))
cobrinha_dir = up

#maçã
maca_pos = (200, 300)
maca_sup = pygame.Surface((10, 10))
maca_sup.fill((255, 0, 0))

#funcionamento do jogo
while True:

    tela.fill((0,0,0))  

    pygame.time.Clock().tick(10)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        if event.type == KEYDOWN:
            if event.key in [left, right, up, down]:
                cobrinha_dir = event.key

    if cobrinha_dir == left:
        nova_posicao = (cobrinha_pos[0][0] - passo, cobrinha_pos[0][1])
    elif cobrinha_dir == right:
        nova_posicao = (cobrinha_pos[0][0] + passo, cobrinha_pos[0][1])
    elif cobrinha_dir == up:
        nova_posicao = (cobrinha_pos[0][0], cobrinha_pos[0][1] - passo)
    elif cobrinha_dir == down:
        nova_posicao = (cobrinha_pos[0][0], cobrinha_pos[0][1] + passo)      

    cobrinha_pos.insert(0, nova_posicao)
    #Desenhando a cobrinha
    for posicao in cobrinha_pos:
        tela.blit(cobrinha_sup, posicao)        
    tela.blit(maca_sup, maca_pos)
    pygame.display.update()        