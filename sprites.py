import pygame
from config import *

class Ingrediente(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 0
    

    def update(self):
        self.rect.x += self.speedx


class Pizza(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.ingredientes = pygame.sprite.Group()
        self.speedx = 3

    def add(self, ingrediente):
        self.ingredientes.add(ingrediente)
        ingrediente.speedx = self.speedx

    def update(self):
        self.rect.x += self.speedx
        if self.rect.x > xt:
            for i in self.ingredientes.sprites():
                i.rect.x = i.rect.x - self.rect.x - 200
            self.rect.x = -200

