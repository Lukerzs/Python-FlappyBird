import pygame

import assets
import config
from objects.background import Background
from objects.bird import Bird
from objects.column import Column
from objects.floor import Floor
from objects.gameOver_message import GameOverMessage
from objects.gameStart_message import GameStartMessage
from objects.score import Score

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()
column_create_event = pygame.USEREVENT
running = True
gameOver = False
gameStarted = False

assets.load_sprites()

sprites = pygame.sprite.LayeredUpdates()


def create_sprites():
    Background(0, sprites)
    Background(1, sprites)
    Floor(0, sprites)
    Floor(1, sprites)

    return Bird(sprites), GameStartMessage(sprites), Score(sprites)


bird, game_start_message, score = create_sprites()

pygame.time.set_timer(column_create_event, 1500)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == column_create_event:
            Column(sprites)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not gameStarted and not gameOver:
                gameStarted = True
                game_start_message.kill()
            if event.key == pygame.K_ESCAPE and gameOver:
                gameOver = False
                gameStarted = False
                sprites.empty()  # clear the sprites table to create a new one
                bird, game_start_message, score = create_sprites()
        bird.handle_event(event)

    sprites.draw(screen)

    if gameStarted and not gameOver:
        sprites.update()

    if bird.check_collision(sprites):
        gameOver = True
        gameStarted = False
        GameOverMessage(sprites)

    for sprite in sprites:
        if type(sprite) is Column and sprite.is_passed():
            score.value += 1

    pygame.display.flip()
    clock.tick(config.FPS)

pygame.quit()
