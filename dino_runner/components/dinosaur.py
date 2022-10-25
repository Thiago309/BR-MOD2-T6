import pygame

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

X_POS = 80
Y_POS = 310
Y_POS_DUCK = 340
JUMP_VEL = 8.5

class Dinosaur:
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect() #pega as dimensões da imagem do dinossauro
        self.dino_rect.x = X_POS #dimensão do eixo X da imagem do dinossauro
        self.dino_rect.y = Y_POS #    ''   '' eixo y ''   ''   ''      ''
        self.step_index = 0     #Conta o movimento das pernas do Dinossauro
        self.dino_run = True    #O dinossauro esta se movendo
        self.dino_jump = False  #O dinossauro não está pulando
        self.dino_duck = False  #O dinossauro não está abaixado
        self.jump_vel = JUMP_VEL

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()


        if self.step_index >= 10:
            self.step_index = 0


        if user_input[pygame.K_w] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_s] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or user_input[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def run(self):   #essa função dar sensação que o dino esta movimentando o passo
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1
     
    def draw(self, screen):  #desenha o objeto na tela, no caso, o dinossauro.
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def duck(self):
        self.image = DUCKING
        if self.dino_duck:
            self.dino_rect = self.image.get_rect() #Ja que ira modificar a posição dinamica do eixo y é necessario atualizar as dimenões novamente.
            self.dino_rect.x = X_POS    
            self.dino_rect.y = Y_POS_DUCK #A dimensão do eixo Y se altera quando o dino abaixa
            self.step_index += 1
        elif not self.dino_duck:
            self.dino_duck = False
      
        