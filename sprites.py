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


'''
O arquivo sprites foi utilizado para a inicialização de imagens e assets
Esta mudança de coesão facilita a localização de variáveis de imagem, assim como deixa o código principal mais limpo

'''
pygame.display.init()

pizza_img = pygame.image.load("imagens\\pizza.png").convert_alpha()
pizza_img = pygame.transform.scale(pizza_img, (350, 350))
image2 = pygame.image.load("imagens\\cardapio.jpg").convert()
image2 = pygame.transform.scale(image2, (xt, yt))
image3 = pygame.image.load("imagens\\fundo.jpg").convert()
image3 = pygame.transform.scale(image3, (xt, yt))
esteira = pygame.image.load("imagens\\esteira.jpg").convert()
esteira = pygame.transform.scale(esteira, (1500, 250))


pizzavazia_img = pygame.image.load("imagens\\pizzasr.png").convert_alpha()
pizzavazia_img = pygame.transform.scale(pizzavazia_img, (200, 200))
madeira = pygame.image.load("imagens\\madeira.png").convert_alpha()
madeira = pygame.transform.scale(madeira, (1100, 200))
duende_img = pygame.image.load("imagens\\duende.png").convert_alpha()
duende_img = pygame.transform.scale(duende_img, (75, 75))
barata_img = pygame.image.load("imagens\\barata1.png").convert_alpha()
barata_img = pygame.transform.scale(barata_img, (75, 75))
sapo_img = pygame.image.load("imagens\\sapo.png").convert_alpha()
sapo_img = pygame.transform.scale(sapo_img, (75, 75))
slime_img = pygame.image.load("imagens\\slime.png").convert_alpha()
slime_img = pygame.transform.scale(slime_img, (75, 120))
zumbi_img = pygame.image.load("imagens\\zumbi.png").convert_alpha()
zumbi_img = pygame.transform.scale(zumbi_img, (75, 75))
bota_img = pygame.image.load("imagens\\bota.png").convert_alpha()
bota_img = pygame.transform.scale(bota_img, (75, 75))
chip_img = pygame.image.load("imagens\\chip.png").convert_alpha()
chip_img = pygame.transform.scale(chip_img, (75, 75))
pimenta_img = pygame.image.load("imagens\\pimenta.png").convert_alpha()
pimenta_img = pygame.transform.scale(pimenta_img, (75, 120))
molhopimen_img = pygame.image.load("imagens\\molhopimen.png").convert_alpha()
molhopimen_img = pygame.transform.scale(molhopimen_img, (120, 120))
molhoslime_img = pygame.image.load("imagens\\molhoslime.png").convert_alpha()
molhoslime_img = pygame.transform.scale(molhoslime_img, (120, 120))
vidas_img = pygame.image.load("imagens\\vidas.png").convert_alpha()
vidas_img = pygame.transform.scale(vidas_img, (25, 25))

comanda = pygame.image.load("imagens\\comanda.png").convert_alpha()
comanda = pygame.transform.scale(comanda, (250, 250))
cursor = pygame.image.load("imagens\\cursor.png").convert_alpha()
cursor = pygame.transform.scale(cursor, (20, 20))