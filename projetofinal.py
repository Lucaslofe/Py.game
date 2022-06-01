# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import *
from sqlalchemy import false

from sprites import Ingrediente, Pizza

pygame.init()
# ----- Gera tela principal
xt = 1100
yt = 650
window = pygame.display.set_mode((xt, yt))
pygame.display.set_caption('py.zza game')
pygame.mouse.set_visible(False)
# ----- Inicia estruturas de dados
game = True
#drag = False (comentada pq estava dando erro)
drag_duende, drag_barata, drag_sapo, drag_slime, drag_zumbi, drag_chip, drag_pimenta, drag_bota = False, False, False, False, False, False, False, False
# ----- Inicia assets
font = pygame.font.SysFont(None, 60)
text_game = font.render('py.zza game', True, (0, 255, 0))
font = pygame.font.SysFont(None, 34)
score = font.render('score: ', True, (51, 51, 255))
font = pygame.font.SysFont(None, 42)
text_press = font.render('press any button to start', True, (255, 0, 0))
pizza_img = pygame.image.load("imagens\\pizza.png").convert_alpha()
pizza_img = pygame.transform.scale(pizza_img, (350, 350))
image2 = pygame.image.load("imagens\\cardapio.jpg").convert()
image2 = pygame.transform.scale(image2, (xt,yt))
image3 = pygame.image.load("imagens\\fundo.jpg").convert()
image3 = pygame.transform.scale(image3, (xt,yt)) 
esteira = pygame.image.load("imagens\\esteira.jpg").convert()
esteira = pygame.transform.scale(esteira,(1500,250))
clock = pygame.time.Clock()
fps = 240
pizzavazia_img = pygame.image.load("imagens\\pizzasr.png").convert_alpha()
pizzavazia_img = pygame.transform.scale(pizzavazia_img, (200, 200))
madeira = pygame.image.load("imagens\\madeira.png").convert_alpha()
madeira = pygame.transform.scale(madeira,(1100,200))

duende_img = pygame.image.load("imagens\\duende.png").convert_alpha()
duende_img = pygame.transform.scale(duende_img, (75,75))
barata_img = pygame.image.load("imagens\\barata1.png").convert_alpha()
barata_img = pygame.transform.scale(barata_img, (75,75))
sapo_img = pygame.image.load("imagens\\sapo.png").convert_alpha()
sapo_img = pygame.transform.scale(sapo_img, (75,75))
slime_img = pygame.image.load("imagens\\slime.png").convert_alpha()
slime_img = pygame.transform.scale(slime_img, (75,120))
zumbi_img = pygame.image.load("imagens\\zumbi.png").convert_alpha()
zumbi_img = pygame.transform.scale(zumbi_img, (75,75))
bota_img = pygame.image.load("imagens\\bota.png").convert_alpha()
bota_img = pygame.transform.scale(bota_img, (75,75))
chip_img = pygame.image.load("imagens\\chip.png").convert_alpha()
chip_img = pygame.transform.scale(chip_img, (75,75))
pimenta_img = pygame.image.load("imagens\\pimenta.png").convert_alpha()
pimenta_img = pygame.transform.scale(pimenta_img, (75,120))

comanda = pygame.image.load("imagens\\comanda.png").convert_alpha()
comanda = pygame.transform.scale(comanda, (250, 250))
cursor = pygame.image.load("imagens\\cursor.png").convert_alpha()
cursor = pygame.transform.scale(cursor, (20,20))

all_sprites = pygame.sprite.Group()
all_ingredientes = pygame.sprite.Group()

ing = {
    0: { "img": duende_img, "x": 330, "y": 267 },
    1: { "img": barata_img, "x": 440, "y": 267 },
    2: { "img": sapo_img, "x": 550, "y": 267 },
    3: { "img": slime_img, "x": 200, "y": 230 },
    4: { "img": zumbi_img, "x": 660, "y": 267 },
    5: { "img": bota_img, "x": 770, "y": 267 },
    6: { "img": chip_img, "x": 880, "y": 267 },
    7: { "img": pimenta_img, "x": 100, "y": 230 }
}

lista_ingredientes = []

for k, v in ing.items():
    ingrediente = Ingrediente(v['img'], v['x'], v['y'])
    lista_ingredientes.append(ingrediente)
    all_ingredientes.add(ingrediente)
    all_sprites.add(ingrediente)


pizza = Pizza(pizzavazia_img, -100, 428)
all_sprites.add(pizza)

fallvel = 3
cond = False
cond2 = True
# ===== Loop principal =====
state = "start_screen"
vel_esteira = 1
x_esteira = -200
x_esteira2 = -1700
x_pizza = -250
clock = pygame.time.Clock()
selecionado = None
while game:
    clock.tick(fps)
    mx, my = pygame.mouse.get_pos()
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
           
    if state == "start_screen":    
        window.blit(image2,(0,0))
        window.blit(pizza_img,(355,150))
        window.blit(text_game, (400, 40))
        window.blit(text_press, (360, 500))
        if event.type == pygame.KEYUP:
            state = "game_screen"
    if state == "game_screen":
        if selecionado != None:
            selecionado.rect.x = mx
            selecionado.rect.y = my
        if event.type == pygame.MOUSEBUTTONDOWN and selecionado == None:
            for i in range(len(lista_ingredientes)):
                r = lista_ingredientes[i].rect
                # print(r.x, r.right, r.y, r.bottom, mx, my)
                if r.x <= mx and mx <= r.right and r.y <= my and my <= r.bottom:
                    item = Ingrediente(ing[i]['img'], mx, my)
                    selecionado = item
                    all_sprites.add(selecionado)
                if r.x > mx and mx > r.right and r.y > my and my < r.bottom:
                    item = Ingrediente(ing[i]['img'], mx, my)
                    selecionado = item
                    all_sprites.remove(ingrediente)
                
        if event.type == pygame.MOUSEBUTTONUP:
            if selecionado != None:
                r = pizza.rect
                if r.x <= mx and mx <= r.right and r.y <= my and my <= r.bottom:
                    pizza.add(selecionado)
                else:
                    selecionado.kill()
            selecionado = None

        window.blit(image3,(0,0))
        window.blit(esteira,(x_esteira,400))
        window.blit(esteira,(x_esteira2,400))
        window.blit(madeira,(0,200))
        window.blit(comanda,(850, 0))
        window.blit(score, (870, 213))
        x_esteira += vel_esteira
        x_esteira2 += vel_esteira
        x_pizza += vel_esteira
        if x_esteira >= 1100:
            x_esteira = -1900
        if x_esteira2 >= 1100:
            x_esteira2 = -1900
#        window.blit(image4,(x_pizza,425))
        if x_pizza > 1300:
            x_pizza = -200
            pizza.ingredientes.empty()
             
                 
        all_sprites.update()
        all_sprites.draw(window)
        window.blit(cursor, ((mx), (my)))

    # Constructor. Pass in the color of the block,
    # and its x and y position

        
        


            
            

    # ----- Gera saídas
    
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados



 #o que falta? 
 #a pizza deve zerar quando termina de passar na esteira (a pizza está zerando, mas não a cada passada na tela)
 #score e contagem de score
 #ingredientes na comanda
 #aumenta a velocidade da esteira e da pizza conforme aumenta o score