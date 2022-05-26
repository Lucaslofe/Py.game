# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from sqlalchemy import false

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
text = font.render('py.zza game', True, (0, 255, 0))
font = pygame.font.SysFont(None, 34)
score = font.render('score: ', True, (51, 51, 255))
font = pygame.font.SysFont(None, 42)
text2 = font.render('press any button to start', True, (255, 0, 0))
image = pygame.image.load("imagens\\pizza.png").convert_alpha()
image = pygame.transform.scale(image, (300, 300))
image2 = pygame.image.load("imagens\\cardapio.jpg").convert()
image2 = pygame.transform.scale(image2, (xt,yt))
image3 = pygame.image.load("imagens\\fundo.jpg").convert()
image3 = pygame.transform.scale(image3, (xt,yt)) 
esteira = pygame.image.load("imagens\\esteira.jpg").convert()
esteira = pygame.transform.scale(esteira,(1500,250))
clock = pygame.time.Clock()
fps = 240
image4 = pygame.image.load("imagens\\pizzasr.png").convert_alpha()
image4 = pygame.transform.scale(image4, (200, 200))
madeira = pygame.image.load("imagens\\madeira.png").convert_alpha()
madeira = pygame.transform.scale(madeira,(1100,200))

duende = pygame.image.load("imagens\\duende.png").convert_alpha()
duende = pygame.transform.scale(duende, (75,75))
barata = pygame.image.load("imagens\\barata1.png").convert_alpha()
barata = pygame.transform.scale(barata, (75,75))
sapo = pygame.image.load("imagens\\sapo.png").convert_alpha()
sapo = pygame.transform.scale(sapo, (75,75))
slime = pygame.image.load("imagens\\slime.png").convert_alpha()
slime = pygame.transform.scale(slime, (75,120))
zumbi = pygame.image.load("imagens\\zumbi.png").convert_alpha()
zumbi = pygame.transform.scale(zumbi, (75,75))
bota = pygame.image.load("imagens\\bota.png").convert_alpha()
bota = pygame.transform.scale(bota, (75,75))
chip = pygame.image.load("imagens\\chip.png").convert_alpha()
chip = pygame.transform.scale(chip, (75,75))
pimenta = pygame.image.load("imagens\\pimenta.png").convert_alpha()
pimenta = pygame.transform.scale(pimenta, (75,120))

comanda = pygame.image.load("imagens\\comanda.png").convert_alpha()
comanda = pygame.transform.scale(comanda, (250, 250))
cursor = pygame.image.load("imagens\\cursor.png").convert_alpha()
cursor = pygame.transform.scale(cursor, (20,20))
fallvel = 3
cond = False
cond2 = True
# ===== Loop principal =====
state = "start_screen"
vel_esteira = 1
x_esteira = -200
x_esteira2 = -1700
x_pizza = -250
while game:
    clock = pygame.time.Clock()
    clock.tick(fps)
    mx, my = pygame.mouse.get_pos()
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
        window.blit(duende,(330, 267))
        window.blit(barata,(440, 267))
        window.blit(sapo,(550, 267))
        window.blit(slime,(100, 230))
        window.blit(zumbi,(660,267))   
        window.blit(bota,(770, 267))
        window.blit(chip,(880, 267))
        window.blit(pimenta,(200, 230))
        window.blit(comanda,(850, 0))
        window.blit(score, (870, 213))
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
        window.blit(cursor, ((mx), (my)))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if window.blit(duende,(330, 267)).collidepoint(mx,my):
                    drag_duende = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drag_duende = False
                dropx, dropy = pygame.mouse.get_pos()
                cond = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if window.blit(barata,(440, 267)).collidepoint(mx,my):
                    drag_barata = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drag_barata = False
                dropx, dropy = pygame.mouse.get_pos()
                cond = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if window.blit(sapo,(550, 267)).collidepoint(mx,my):
                    drag_sapo = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drag_sapo = False
                dropx, dropy = pygame.mouse.get_pos()
                cond = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if window.blit(slime,(100, 230)).collidepoint(mx,my):
                    drag_slime = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drag_slime = False
                dropx, dropy = pygame.mouse.get_pos()
                cond = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if window.blit(zumbi,(660, 267)).collidepoint(mx,my):
                    drag_zumbi = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drag_zumbi = False
                dropx, dropy = pygame.mouse.get_pos()
                cond = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if window.blit(bota,(770, 267)).collidepoint(mx,my):
                    drag_bota = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drag_bota = False
                dropx, dropy = pygame.mouse.get_pos()
                cond = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if window.blit(chip,(880, 267)).collidepoint(mx,my):
                    drag_chip = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drag_chip = False
                dropx, dropy = pygame.mouse.get_pos()
                cond = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if window.blit(pimenta,(200, 230)).collidepoint(mx,my):
                    drag_pimenta = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drag_pimenta = False
                dropx, dropy = pygame.mouse.get_pos()
                cond = True
                    
        if drag_duende == True:
            window.blit(duende,((mx-50),(my-50)))
        elif drag_duende == False and cond == True: #(tentativa de fazer o ingrediente cair, mas fica spawnando duende toda vez que clica)
             window.blit(duende,(x_pizza, 450))
             #dropy += fallvel
             #window.blit(duende,((dropx-10),(dropy-10)))

        if drag_barata == True:
            window.blit(barata,((mx-50),(my-50)))

        if drag_sapo == True:
            window.blit(sapo,((mx-50),(my-50)))

        if drag_slime == True:
            window.blit(slime,((mx-50),(my-50)))

        if drag_zumbi == True:
            window.blit(zumbi,((mx-50),(my-50)))

        if drag_bota == True:
            window.blit(bota,((mx-50),(my-50)))

        if drag_chip == True:
            window.blit(chip,((mx-50),(my-50)))

        if drag_pimenta == True:
            window.blit(pimenta,((mx-50),(my-50)))




    # Constructor. Pass in the color of the block,
    # and its x and y position

        
        


            
            

    # ----- Gera saídas
    
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

 