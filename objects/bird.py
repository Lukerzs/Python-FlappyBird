import pygame.sprite

import assets
import config
from layer import Layer


class Bird(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.PLAYER

        self.images = [
            assets.get_sprite('redbird-upflap'),
            assets.get_sprite('redbird-midflap'),
            assets.get_sprite('redbird-downflap')
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=(-50, 50))

        self.flap=0

        super().__init__(*groups)

    def update(self):
        self.images.insert(0,self.images.pop())
        self.image = self.images[0]

        self.flap += config.GRAVITY
        self.rect.y += self.flap

        if self.rect.x < 50:
            self.rect.x += 3

    def handle_event(self,event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.flap = 0
            self.flap -= 7

