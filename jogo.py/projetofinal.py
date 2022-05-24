# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
xt = 1100
yt = 650
window = pygame.display.set_mode((xt, yt))
pygame.display.set_caption('py.zza game')

# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
font = pygame.font.SysFont(None, 60)
text = font.render('py.zza game', True, (0, 255, 0))
font = pygame.font.SysFont(None, 42)
text2 = font.render('press any button to start', True, (255, 0, 0))
image = pygame.image.load("pizza.png").convert_alpha()
image = pygame.transform.scale(image, (300, 300))
image2 = pygame.image.load("cardapio.jpg").convert()
image2 = pygame.transform.scale(image2, (xt,yt))
image3 = pygame.image.load("fundo.jpg").convert()
image3 = pygame.transform.scale(image3, (xt,yt)) 
esteira = pygame.image.load("esteira.jpg").convert()
esteira = pygame.transform.scale(esteira,(1500,250))
clock = pygame.time.Clock()
fps = 30
image4 = pygame.image.load("pizzasr.png").convert_alpha()
image4 = pygame.transform.scale(image4, (200, 200))
madeira = pygame.image.load("madeira.png").convert_alpha()
madeira = pygame.transform.scale(madeira,(1100,200))
duende = pygame.image.load("duende.png").convert_alpha()
duende = pygame.transform.scale(duende, (1,1))
barata = pygame.image.load("barata.png").convert_alpha()
barata = pygame.transform.scale(barata, (1,1))
sapo = pygame.image.load("sapo.png").convert_alpha()
sapo = pygame.transform.scale(sapo, (1,1))
slime = pygame.image.load("slime.png").convert_alpha()
slime = pygame.transform.scale(slime, (1,1))
zumbi = pygame.image.load("zumbi.png").convert_alpha()
zumbi = pygame.transform.scale(zumbi, (1,1))
bota = pygame.image.load("bota.png").convert_alpha()
bota = pygame.transform.scale(bota, (1,1))
chip = pygame.image.load("chip.png").convert_alpha()
chip = pygame.transform.scale(chip, (1,1))
pimenta = pygame.image.load("pimenta.png").convert_alpha()
pimenta = pygame.transform.scale(pimenta, (1,1))


# ===== Loop principal =====
state = "start_screen"
vel_esteira = 5
x_esteira = -200
x_esteira2 = -1700
x_pizza = -250
while game:
    clock = pygame.time.Clock()
    clock.tick(fps)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    if state == "start_screen":    
        window.blit(image2,(0,0))
        window.blit(text, (420, 40))
        window.blit(image,(400,150))
        window.blit(text2, (380, 500))
        if event.type == pygame.KEYUP:
            state = "game_screen"
    if state == "game_screen":
        window.blit(image3,(0,0))
        window.blit(esteira,(x_esteira,400))
        window.blit(esteira,(x_esteira2,400))
        window.blit(madeira,(0,200))
        x_esteira += vel_esteira
        x_esteira2 += vel_esteira
        x_pizza += vel_esteira
        if x_esteira >= 1100:
            x_esteira = -1900
        if x_esteira2 >= 1100:
            x_esteira2 = -1900
        window.blit(image4,(x_pizza,425))
        if x_pizza > 1100:
            x_pizza = -200
        


            
            

    # ----- Gera saídas
    #cor = (0,255,0)
    #vertices = [(400,400),(700,400),(700,500),(400,500)]
    #pygame.draw.polygon(window,cor,vertices)
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

#peperoni, palmito, queijo, milho, ervilha, cebola,   