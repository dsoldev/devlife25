import pygame
import random


def inicializa():
    pygame.init()
    window = pygame.display.set_mode((640, 480))

    assets = {
        'jogador': pygame.image.load('player.png'),
        'chicken_frames': [
            pygame.image.load('chicken_01.png'),
            pygame.image.load('chicken_02.png')
        ]
    }

    state = {
        'jogador_x': 320, 
        'jogador_y': 240,
        'jogador_vx': 2,
        'jogador_vy': 2,
        'chicken_x': 100,
        'chicken_y': 100,
        'chicken_vx': 0.1,
        'chicken_vy': 0.1,
        'chicken_frame': 0,
        'chicken_animation_counter': 0
    }

    return window, assets, state


def desenha(window, assets, state):
    window.fill((0, 0, 0))  # Limpa a tela com preto
    # Desenha o jogador na posição atual
    window.blit(assets['jogador'], (state['jogador_x'], state['jogador_y']))
    # Desenha a galinha com o frame de animação atual
    current_chicken_frame = assets['chicken_frames'][state['chicken_frame']]
    window.blit(current_chicken_frame, (state['chicken_x'], state['chicken_y']))
    pygame.display.update()


def recebe_eventos(state):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False
        # Detecta quando a tecla SPACE é pressionada
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                # Teletransporta a galinha para uma posição aleatória
                state['chicken_x'] = random.randint(0, 640 - 32)
                state['chicken_y'] = random.randint(0, 480 - 32)
    
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
    state['jogador_x'] = max(0, min(state['jogador_x'], 640 - 32))  # Assumindo largura do jogador de 32px
    state['jogador_y'] = max(0, min(state['jogador_y'], 480 - 32))  # Assumindo altura do jogador de 32px
    
    # Move a galinha na direção oposta ao jogador
    # Calcula a direção da galinha para o jogador
    dx = state['jogador_x'] - state['chicken_x']
    dy = state['jogador_y'] - state['chicken_y']
    
    # Move a galinha para longe do jogador (direção oposta)
    if dx > 0:  # Jogador está à direita, move a galinha para a esquerda
        state['chicken_x'] -= state['chicken_vx']
    elif dx < 0:  # Jogador está à esquerda, move a galinha para a direita
        state['chicken_x'] += state['chicken_vx']
        
    if dy > 0:  # Jogador está abaixo, move a galinha para cima
        state['chicken_y'] -= state['chicken_vy']
    elif dy < 0:  # Jogador está acima, move a galinha para baixo
        state['chicken_y'] += state['chicken_vy']

    
    # Mantém a galinha dentro dos limites da tela
    state['chicken_x'] = max(0, min(state['chicken_x'], 640 - 32))  # Assumindo largura da galinha de 32px
    state['chicken_y'] = max(0, min(state['chicken_y'], 480 - 32))  # Assumindo altura da galinha de 32px
    
    # Atualiza animação da galinha
    state['chicken_animation_counter'] += 1
    if state['chicken_animation_counter'] >= 10:  # Troca de frame a cada 10 loops do jogo
        state['chicken_frame'] = 1 - state['chicken_frame']  # Alterna entre 0 e 1
        state['chicken_animation_counter'] = 0


if __name__ == '__main__':
    window, assets, state = inicializa()
    while recebe_eventos(state):
        atualiza_estado(state)
        desenha(window, assets, state)
