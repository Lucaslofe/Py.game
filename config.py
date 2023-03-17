import pygame
'''
 o arquivo config foi utilizado para inicializar variáveis fixas e ajustes de demais variáveis

 Valores fixos foram substituídos por variáveis com o objetivo de diminuir a utilização de memória do computador

 Esta abstração foi feita com o intuito de facilitar possíveis mudanças futuras, como atualização de posições de 
 sprites e redefição dimensoes de tela.
'''

game = True
drag_duende, drag_barata, drag_sapo, drag_slime, drag_zumbi, drag_chip, drag_pimenta, drag_bota = False, False, False, False, False, False, False, False

xt = 1100
yt = 650

fps = 30
y_ing = 267
ajuste = -37

pontos = 0
vidas = 3

x_ing = 110
#vel_esteira = 4
x_esteira = -200
x_esteira2 = -1700
x_pizza = -200

'''
x_esteira += vel_esteira
x_esteira2 += vel_esteira
x_pizza += vel_esteira
'''


# ----- Gera tela principal
pygame.display.init()
pygame.font.init()

window = pygame.display.set_mode((xt, yt))
pygame.display.set_caption('py.zza game')
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 60)
text_game = font.render('py.zza game', True, (0, 255, 0))
font = pygame.font.SysFont(None, 42)
text_press = font.render('press any button to start', True, (255, 0, 0))