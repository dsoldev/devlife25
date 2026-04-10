import pygame

class Player:
    def __init__(self, x=512, y=384):
        self.x = x 
        self.y = y
        self.jogador_vx = 1
        self.jogador_vy = 1
        self.sprite = pygame.image.load('player.png')

    def desenha(self, window):
        window.blit(self.sprite, (self.x, self.y))
    
    def recebe_eventos(self, keys):
            # Atualiza posição do jogador baseado nas teclas pressionadas
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.jogador_vx
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.jogador_vx
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.jogador_vy
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.jogador_vy
    
    def update(self):
        # Mantém o jogador dentro dos limites da tela
        self.x = max(0, min(self.x, 1024 - 32))  # Assumindo largura do jogador de 32px
        self.y = max(0, min(self.y, 768 - 32))  # Assumindo altura do jogador de 32px

class Chicken:
    
    def __init__(self, x, y, vx = 0.5, vy = 0.5):
       self.x = x 
       self.y = y 
       self.vx = vx 
       self.vy = vy
       self.frame_atual = 0 
       self.animation_counter = 0
       self.frames =  [
            pygame.image.load('chicken_01.png'),
            pygame.image.load('chicken_02.png')
        ]
       


    def move_galinha(self, player): 
        # Move a galinha na direção oposta ao jogador
        # Calcula a direção da galinha para o jogador
        dx = player.x - self.x
        dy = player.y - self.y

        move_x = 0
        move_y = 0
        
        # Move a galinha para longe do jogador (direção oposta)
        if dx > 0:  # Jogador está à direita, move a galinha para a esquerda
            move_x = -self.vx
        elif dx < 0:  # Jogador está à esquerda, move a galinha para a direita
            move_x = self.vx
            
        if dy > 0:  # Jogador está abaixo, move a galinha para cima
            move_y = -self.vy
        elif dy < 0:  # Jogador está acima, move a galinha para baixo
            move_y = self.vy

        max_x = 1024 - 32  # Assumindo largura da galinha de 32px
        max_y = 768 - 32  # Assumindo altura da galinha de 32px

        # Se o movimento empurra para fora da tela, inverte o eixo para destravar cantos.
        next_x = self.x + move_x
        next_y = self.y + move_y

        if next_x < 0 or next_x > max_x:
            move_x = -move_x
        if next_y < 0 or next_y > max_y:
            move_y = -move_y

        self.x += move_x
        self.y += move_y

        
        # Mantém a galinha dentro dos limites da tela
        self.x = max(0, min(self.x, max_x))
        self.y = max(0, min(self.y, max_y))
        
        # Atualiza animação da galinha
        self.animation_counter += 1
        if self.animation_counter >= 10:  # Troca de frame a cada 10 loops do jogo
            self.frame_atual = 1 - self.frame_atual  # Alterna entre 0 e 1
            self.animation_counter = 0
    
    def desenha_galinha(self, window):
            window.blit(self.frames[self.frame_atual], (self.x, self.y))
