import pygame
import os

WIDTH = 800
HEIGHT = 600
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# ???
pygame.init()
pygame.mixer.init()     # ????
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("????")
clock = pygame.time.Clock()
all_sprite = pygame.sprite.Group()

game_floder = os.path.dirname(__file__)
img_floder = os.path.join(game_floder, "image")

class Player(pygame.sprite.Sprite):
        def __init__(self):
                    pygame.sprite.Sprite.__init__(self)
                            self.image = pygame.image.load(os.path.join(img_floder, "plane11.png")).convert()
                                    self.image.set_colorkey(WHITE)      # ????
                                            self.rect = self.image.get_rect()
                                                    self.rect.center = (int(WIDTH/2), int(HEIGHT/2))
                                                            self.y_speed = 5
                                                                    self.x_speed = 5

                                                                        def update(self):
                                                                                    self.rect.x += self.x_speed
                                                                                            self.rect.y += self.y_speed
                                                                                                    # ???
                                                                                                            if self.rect.bottom > HEIGHT - 250:
                                                                                                                            self.y_speed = -5
                                                                                                                                    if self.rect.top < 250:
                                                                                                                                                    self.y_speed = 5
                                                                                                                                                            if self.rect.right > WIDTH:
                                                                                                                                                                            self.rect.left = 0

                                                                                                                                                                            player = Player()
                                                                                                                                                                            all_sprite.add(player)

# ???
running = True
while running:
        clock.tick(FPS)
            for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                        running = False

                                            all_sprite.update()

                                                screen.fill(GREEN)
                                                    all_sprite.draw(screen)
                                                        pygame.display.flip()

                                                        pygame.quit()
