import pygame

class Player:
    def __init__(self, x=0, y=0):
        self.x = x 
        self.y = y


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
        
        # Move a galinha para longe do jogador (direção oposta)
        if dx > 0:  # Jogador está à direita, move a galinha para a esquerda
            self.x -= self.vx
        elif dx < 0:  # Jogador está à esquerda, move a galinha para a direita
            self.x += self.vx
            
        if dy > 0:  # Jogador está abaixo, move a galinha para cima
            self.y -= self.vy
        elif dy < 0:  # Jogador está acima, move a galinha para baixo
            self.y += self.vy

        
        # Mantém a galinha dentro dos limites da tela
        self.x = max(0, min(self.x, 1024 - 32))  # Assumindo largura da galinha de 32px
        self.y = max(0, min(self.y, 768 - 32))  # Assumindo altura da galinha de 32px
        
        # Atualiza animação da galinha
        self.animation_counter += 1
        if self.animation_counter >= 10:  # Troca de frame a cada 10 loops do jogo
            self.frame_atual = 1 - self.frame_atual  # Alterna entre 0 e 1
            self.animation_counter = 0
    
    def desenha_galinha(self, window):
            window.blit(self.frames[self.frame_atual], (self.x, self.y))
