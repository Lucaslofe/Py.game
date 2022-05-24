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
fps = 15
# ===== Loop principal =====
state = "start_screen"
vel_esteira = 3
x_esteira = -200
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
        x_esteira += vel_esteira
        if x_esteira >= 0:
            x_esteira = -200

            
            

    # ----- Gera saídas
    #cor = (0,255,0)
    #vertices = [(400,400),(700,400),(700,500),(400,500)]
    #pygame.draw.polygon(window,cor,vertices)
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados