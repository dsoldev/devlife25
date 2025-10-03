import pygame
import random
from chicken import *




def inicializa():
    pygame.init()
    window = pygame.display.set_mode((1024, 768))


    assets = {
        'jogador': pygame.image.load('player.png'),         
    }


    n_galinhas = 12
    galinhas = []

    for i in range(n_galinhas): 
        galinha = Chicken(random.randint(100,700),random.randint(200, 400))
        galinhas.append(galinha)

    state = {
        'jogador_x': 512, 
        'jogador_y': 384,
        'jogador_vx': 1,
        'jogador_vy': 1,
        'cor_fundo' : (74, 115, 157),
        'chickens': galinhas

    }

    return window, assets, state


def desenha(window, assets, state):
    window.fill(state['cor_fundo'])  # Limpa a tela com preto
    # Desenha o jogador na posição atual
    window.blit(assets['jogador'], (state['jogador_x'], state['jogador_y']))
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

    # Atualiza posição do jogador baseado nas teclas pressionadas
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        state['jogador_x'] -= state['jogador_vx']
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        state['jogador_x'] += state['jogador_vx']
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        state['jogador_y'] -= state['jogador_vy']
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        state['jogador_y'] += state['jogador_vy']


    return True


def atualiza_estado(state):
    # Mantém o jogador dentro dos limites da tela
    state['jogador_x'] = max(0, min(state['jogador_x'], 1024 - 32))  # Assumindo largura do jogador de 32px
    state['jogador_y'] = max(0, min(state['jogador_y'], 768 - 32))  # Assumindo altura do jogador de 32px

    # Criando player só para chamar o move_galinha
    player = Player(state['jogador_x'], state['jogador_y'])
    for g in state["chickens"]:
        g.move_galinha(player)
    


if __name__ == '__main__':
    window, assets, state = inicializa()
    while recebe_eventos(state):
        atualiza_estado(state)
        desenha(window, assets, state)
