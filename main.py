import pygame

import assets
import config
from objects.background import Background
from objects.bird import Bird
from objects.column import Column
from objects.floor import Floor

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()
column_create_event = pygame.USEREVENT
running = True

assets.load_sprites()

sprites = pygame.sprite.LayeredUpdates()

Background(0, sprites)
Background(1, sprites)
Floor(0, sprites)
Floor(1, sprites)

bird = Bird(sprites)

pygame.time.set_timer(column_create_event, 1500)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == column_create_event:
            Column(sprites)
        bird.handle_event(event)

    sprites.draw(screen)
    sprites.update()

    pygame.display.flip()
    clock.tick(config.FPS)

pygame.quit()
