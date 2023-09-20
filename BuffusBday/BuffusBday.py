import statistics
from typing import Any
import pygame

WIDTH = 1200
HEIGHT = 600
SPEED = 35
GAME_SPEED = 35
GROUND_WIDTH = 1200
GROUND_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_run = [
                          pygame.image.load('sprites/capi1.png').convert_alpha(),
                          pygame.image.load('sprites/capi2.png').convert_alpha()
                          ]
        self.image = pygame.image.load('sprites/capi1.png').convert_alpha()
        self.rect = pygame.Rect(100, 100, 100, 100)
        self.current_image = 0

    def update(self, *args):
        def move_player(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_d]:
                self.rect[0] += GAME_SPEED
            if key[pygame.K_a]:
                self.rect[0] -= GAME_SPEED
            self.current_image = (self.current_image + 1) % 2
            self.image = self.image_run[self.current_image]
            self.image = pygame.transform.scale(self.image, [100, 100])
        move_player(self)
        self.rect[1] -= SPEED

class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/background4.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect [0] = xpos
        self.rect [1] = HEIGHT - GROUND_HEIGHT

    def update(self, *args):
        self.rect[0] -= GAME_SPEED

def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

pygame.init()

game_window = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Buffus' Bday")

BACKGROUND = pygame.image.load('sprites/background3.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, [WIDTH, HEIGHT])

playerGroup = pygame.sprite.Group()
player = Player()
playerGroup.add(player)

groundGroup = pygame.sprite.Group()
for i in range(2):
    ground = Ground(WIDTH * i)
    groundGroup.add(ground)


gameloop = True
def draw():
    #game_window.fill([230, 255, 255])
    playerGroup.draw(game_window)
    groundGroup.draw(game_window)


def update():
    playerGroup.update()
    groundGroup.update()

clock = pygame.time.Clock()

while gameloop:
    clock.tick(5)
    game_window.blit(BACKGROUND, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    if is_off_screen(groundGroup.sprites()[0]):
        groundGroup.remove(groundGroup.sprites()[0])
        newGround = Ground(WIDTH - 35)
        groundGroup.add(newGround)

    if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
        SPEED = 0
        print ('collision')
    else:
        SPEED = 35

    update()
    draw()
    pygame.display.update()