# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((1100, 650))
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
# ===== Loop principal =====

while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYUP:
            game = False
            

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(text, (420, 40))
    window.blit(image,(400,150))
    window.blit(text2, (380, 500))
    #cor = (0,255,0)
    #vertices = [(400,400),(700,400),(700,500),(400,500)]
    #pygame.draw.polygon(window,cor,vertices)
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados