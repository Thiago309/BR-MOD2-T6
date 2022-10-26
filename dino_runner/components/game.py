import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)   #titulo da janela do game
        pygame.display.set_icon(ICON)       #icone da janela do game 
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #define as dimensões da janela do game
        self.clock = pygame.time.Clock() #usando o metodo do pygame relogio
        self.playing = False  
        self.game_speed = 20  #velocidade em que o jogo ocorre
        self.x_pos_bg = 0    #posicionamento da janela eixo x
        self.y_pos_bg = 380  #      ''       ''   '' eixo y
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()

    def run(self):  #metodo que executa o jogo
        # Game loop: events - update - draw
        self.playing = True
        while self.playing: 
            self.events()  #executa o jogo
            self.update()  #atualiza as imagens do game
            self.draw()    #desenha no bg
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) # #ffffff
        self.draw_background()
        self.player.draw(self.screen)
<<<<<<< HEAD
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()
=======
        pygame.display.update()  #desenha na tele que esta em constante atualização
        pygame.display.flip()    #ordena oque vai ser desenhado na tela
>>>>>>> 6ce312835cb9bbb87faf90863226cc8d91da3069

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
