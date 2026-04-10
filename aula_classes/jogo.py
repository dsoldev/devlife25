import pygame
import random
from chicken import *

def inicializa():
    pygame.init()
    window = pygame.display.set_mode((1024, 768))


    assets = {}


    n_galinhas = 12
    galinhas = []

    for i in range(n_galinhas): 
        galinha = Chicken(random.randint(100,700),random.randint(200, 400))
        galinhas.append(galinha)

    state = {
        'cor_fundo' : (74, 115, 157),
        'chickens': galinhas,
        'player': Player()
    }

    return window, assets, state


def desenha(window, assets, state):
    window.fill(state['cor_fundo'])  # Limpa a tela com preto
    # Desenha o jogador na posição atual
    state['player'].desenha(window)
    # Desenha a galinha com o frame de animação atual
    for g in state["chickens"]:
        g.desenha_galinha(window)

    pygame.display.update()


def recebe_eventos(state):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False
        # Detecta quando a tecla SPACE é pressionada
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                # Teletransporta a galinha para uma posição aleatória
                state['chicken'].x = random.randint(0, 1024 - 32)
                state['chicken'].y = random.randint(0, 768 - 32)
    
    keys = pygame.key.get_pressed()
    state['player'].recebe_eventos(keys)

    return True


def atualiza_estado(state):
    for g in state["chickens"]:
        g.move_galinha(state['player'])
    


if __name__ == '__main__':
    window, assets, state = inicializa()
    while recebe_eventos(state):
        atualiza_estado(state)
        desenha(window, assets, state)
