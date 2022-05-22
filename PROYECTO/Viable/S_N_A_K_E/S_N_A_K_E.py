# Bibliotecas requeridas ----------------------------------------------------------------- #
from asyncio.constants import LOG_THRESHOLD_FOR_CONNLOST_WRITES
from matplotlib.font_manager import list_fonts
import pygame, sys, random, time
# Importación de archivos (* es para importar todas las funciones)
from LLC import *
# Inicializar la pestaña ----------------------------------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('S N A K E E E E E E E E E E E E')
# Tamaño de la pantalla ------------------------------------------------------------------ #
dis_width = 800
dis_height = 600
dis_center = dis_width/2
# Inicializar nuestra pantalla ----------------------------------------------------------- #
dis = pygame.display.set_mode((dis_width, dis_height),0,32)
clock = pygame.time.Clock()
# Velocidad de nuestro poderoso snake ---------------------------------------------------- #
snake_block = 10
snake_speed = 15
#Tipografías a usar ---------------------------------------------------------------------- #
font = pygame.font.SysFont("bahnschrift", 60)
font50 = pygame.font.SysFont("bahnschrift", 50)
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 35)
# Definición de colores para un rápido uso ----------------------------------------------- #
white = (255, 255, 255)
white_S = (100, 100, 100)
yellow = (255, 255, 102)
yellow_S = (100, 100, 40)
black = (0, 0, 0)
red = (255, 0, 0)
red_S = (100, 0, 0)
rojo_que_no_parece_red = (213, 50, 80)
rojo_no_tan_red = (100, 0, 0)
green = (0, 255, 0)
green_S = (0, 100, 0)
blue = (50, 153, 213)
blue_S = (10, 70, 100)
# Inicializamos el click ----------------------------------------------------------------- #
click = False
# Importamos los sonidos
def cargar_sonidos():
    global GameSel
    global AppleBite
    global Snakeeeeee
    global Die
    global Vol
    global MCoin
    global BackM
    GameSel = pygame.mixer.Sound("PROYECTO/Viable/S_N_A_K_E/Sonidos/Select.mp3")
    AppleBite = pygame.mixer.Sound("PROYECTO/Viable/S_N_A_K_E/Sonidos/AppleBite.mp3")
    Snakeeeeee = pygame.mixer.Sound("PROYECTO/Viable/S_N_A_K_E/Sonidos/Snakeeeee.mp3")
    Die = pygame.mixer.Sound("PROYECTO/Viable/S_N_A_K_E/Sonidos/GO.wav")
    Vol = pygame.mixer.Sound("PROYECTO/Viable/S_N_A_K_E/Sonidos/Volumen.mp3")
    MCoin = pygame.mixer.Sound("PROYECTO/Viable/S_N_A_K_E/Sonidos/MCoin.wav")
    BackM = pygame.mixer.Sound("PROYECTO/Viable/S_N_A_K_E/Sonidos/BackMusic.mp3")
    if pygame.mixer.get_init() != None:
        pygame.mixer.set_reserved(2) # reserves channels for the thrust sound and the saucer sound
        pygame.mixer.Channel(1).set_volume(0.5)
# Función para ajustar el volumen
def ajustar_volumen(volume):
    GameSel.set_volume(volume)
    AppleBite.set_volume(volume)
    #Snakeeeeee.set_volume(volume)
    Die.set_volume(volume)
    Vol.set_volume(volume)
    MCoin.set_volume(volume)
    BackM.set_volume(volume)
# Función para dibujar en la pantalla
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
# Función para mostrar el texto de la puntuación ---------------------------------------- #
def Your_score(score):
    value = score_font.render("Tu puntuación: " + str(score), True, white)
    dis.blit(value, [0, 0])
# Propiedades de nuestra serpiente
def our_snake(snake_block, snake_list, colorSk):
    for x in snake_list:
        pygame.draw.rect(dis, colorSk.data, [x[0], x[1], snake_block, snake_block])
# Otra forma de imprimir en pantalla
def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / x, dis_height / y])
# Menú principal
def main_menu():
    cargar_sonidos()
    BackM.play()
    volumen = 100
    score1 = 0
    # Colores del snake
    list_double = double_linked()
    list_double.append('green')
    list_double.append('blue')
    list_double.append('red')
    list_double.append('yellow')
    # Colores del bloque
    listaaa = double_linked()
    listaaa.append('red')
    listaaa.append('blue')
    listaaa.append('yellow')
    listaaa.append('green')
    colorSk = list_double.head
    colorBlock = listaaa.head
    while True:
        dis.fill((black))
        draw_text('S N A K E E E E E E E E E E E E', font, white_S, dis, 105, 25)
        draw_text('S N A K E E E E E E E E E E E E', font, white, dis, 100, 20)
        mx, my = pygame.mouse.get_pos()
        botonx = dis_center-100
        boton_1S = pygame.Rect(botonx+10, 110, 200, 50)
        boton_2S = pygame.Rect(botonx+10, 210, 200, 50)
        boton_3S = pygame.Rect(botonx+10, 310, 200, 50)
        boton_4S = pygame.Rect(botonx+10, 410, 200, 50)
        boton_1 = pygame.Rect(botonx, 100, 200, 50)
        boton_2 = pygame.Rect(botonx, 200, 200, 50)
        boton_3 = pygame.Rect(botonx, 300, 200, 50)
        boton_4 = pygame.Rect(botonx, 400, 200, 50)
        if boton_1.collidepoint((mx, my)):
            if click:
                MCoin.play()
                game_over = False
                game_close = False
                x1 = dis_width / 2
                y1 = dis_height / 2
                x1_change = 0
                y1_change = 0
                snake_List = []
                Length_of_snake = 1
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                while not game_over:
                    while game_close == True:
                        Die.play()
                        dis.fill(rojo_no_tan_red)
                        draw_text('Te moriste, pensé que durarías más ):', font50, white, dis, 100, 100)
                        mx, my = pygame.mouse.get_pos()
                        botonx = dis_center-100
                        boton_2 = pygame.Rect(botonx, 350, 200, 50)
                        pygame.draw.rect(dis, black, boton_2)
                        pygame.draw.rect(dis, red, boton_2, 3)
                        dis.blit(font_style.render("Menú principal", True, white), (botonx+45, 366))
                        """if boton_1.collidepoint((mx, my)):
                            if click:
                                GameSel.play()"""
                        if boton_2.collidepoint((mx, my)):
                            if click:
                                GameSel.play()
                                game_over = True
                                game_close = False
                        click = False
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                            if event.type == KEYDOWN:
                                if event.key == K_q:
                                    game_over = True
                                    game_close = False
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True
                        score1 = Length_of_snake - 1
                        Your_score(Length_of_snake - 1)
                        pygame.display.update()
                        mainClock.tick(60)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game_over = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                x1_change = -snake_block
                                y1_change = 0
                            elif event.key == pygame.K_RIGHT:
                                x1_change = snake_block
                                y1_change = 0
                            elif event.key == pygame.K_UP:
                                y1_change = -snake_block
                                x1_change = 0
                            elif event.key == pygame.K_DOWN:
                                y1_change = snake_block
                                x1_change = 0
                    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                        game_close = True
                    x1 += x1_change
                    y1 += y1_change
                    dis.fill(black)
                    # Color del bloque
                    pygame.draw.rect(dis, colorBlock.data, [foodx, foody, snake_block, snake_block])
                    snake_Head = []
                    snake_Head.append(x1)
                    snake_Head.append(y1)
                    snake_List.append(snake_Head)
                    if len(snake_List) > Length_of_snake:
                        del snake_List[0]
                    for x in snake_List[:-1]:
                        if x == snake_Head:
                            game_close = True
                    our_snake(snake_block, snake_List, colorSk)
                    score2 = Length_of_snake - 1
                    Your_score(Length_of_snake - 1)
                    print("score2: " + str(score2))
                    pygame.display.update()
                    if x1 == foodx and y1 == foody:
                        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                        Length_of_snake += 1
                        AppleBite.play()
                    clock.tick(snake_speed)
        elif boton_2.collidepoint((mx, my)):
            if click:
                GameSel.play()
                running = True
                while running:
                    dis.fill((black))
                    draw_text('Opciones', font, white, dis, 100, 20)
                    mx, my = pygame.mouse.get_pos()
                    boton_atras = pygame.Rect(25, 15, 50, 50)
                    boton_atras_S = pygame.Rect(30, 20, 50, 50)
                    pygame.draw.rect(dis, white_S, boton_atras_S, 10)
                    pygame.draw.rect(dis, black, boton_atras)
                    pygame.draw.rect(dis, white, boton_atras, 3)
                    dis.blit(font.render("<-", True, white), (30, 19))
                    # Volumen
                    botonx = dis_center-100
                    boton_Vol_S = pygame.Rect(botonx+10, 110, 200, 50)
                    boton_Vol = pygame.Rect(botonx, 100, 200, 50)
                    pygame.draw.rect(dis, black, boton_Vol)
                    pygame.draw.rect(dis, white, boton_Vol, 3)
                    dis.blit(font_style.render("Volumen: " + str(volumen), True, white), (botonx+45, 116))

                    boton_UpV_S = pygame.Rect(botonx+260, 110, 50, 50)
                    boton_UpV = pygame.Rect(botonx+250, 100, 50, 50)
                    pygame.draw.rect(dis, green_S, boton_UpV_S, 10)
                    pygame.draw.rect(dis, black, boton_UpV)
                    pygame.draw.rect(dis, green, boton_UpV, 3)
                    dis.blit(font50.render("+", True, green), (botonx+265, 107))

                    boton_DnV_S = pygame.Rect(botonx-100, 110, 50, 50)
                    boton_DnV = pygame.Rect(botonx-110, 100, 50, 50)
                    pygame.draw.rect(dis, red_S, boton_DnV_S, 10)
                    pygame.draw.rect(dis, black, boton_DnV)
                    pygame.draw.rect(dis, red, boton_DnV, 3)
                    dis.blit(font50.render("-", True, red), (botonx-90, 107))

                    # Color Snake
                    # TODO: Reparar lista de colores
                    print('Color del snake: ' + str(colorSk.data))
                    boton_Sk_S = pygame.Rect(botonx+10, 210, 200, 50)
                    boton_Sk = pygame.Rect(botonx, 200, 200, 50)
                    pygame.draw.rect(dis, black, boton_Sk)
                    pygame.draw.rect(dis, colorSk.data, boton_Sk, 3)
                    dis.blit(font_style.render("Color del Snake", True, colorSk.data), (botonx+40, 216))

                    boton_UpC_S = pygame.Rect(botonx+260, 210, 50, 50)
                    boton_UpC = pygame.Rect(botonx+250, 200, 50, 50)
                    pygame.draw.rect(dis, white_S, boton_UpC_S, 10)
                    pygame.draw.rect(dis, black, boton_UpC)
                    pygame.draw.rect(dis, colorSk.data, boton_UpC, 3)
                    dis.blit(font50.render("->", True, colorSk.data), (botonx+260, 207))

                    boton_DnC_S = pygame.Rect(botonx-100, 210, 50, 50)
                    boton_DnC = pygame.Rect(botonx-110, 200, 50, 50)
                    pygame.draw.rect(dis, white_S, boton_DnC_S, 10)
                    pygame.draw.rect(dis, black, boton_DnC)
                    pygame.draw.rect(dis, colorSk.data, boton_DnC, 3)
                    dis.blit(font50.render("<-", True, colorSk.data), (botonx-100, 207))

                    # Color Bloque
                    boton_Block_S = pygame.Rect(botonx+10, 310, 200, 50)
                    boton_Block = pygame.Rect(botonx, 300, 200, 50)
                    pygame.draw.rect(dis, black, boton_Block)
                    pygame.draw.rect(dis, colorBlock.data, boton_Block, 3)
                    dis.blit(font_style.render("Color del Snake", True, colorBlock.data), (botonx+40, 316))

                    boton_BlockUp_S = pygame.Rect(botonx+260, 310, 50, 50)
                    boton_BlockUp = pygame.Rect(botonx+250, 300, 50, 50)
                    pygame.draw.rect(dis, white_S, boton_BlockUp_S, 10)
                    pygame.draw.rect(dis, black, boton_BlockUp)
                    pygame.draw.rect(dis, colorBlock.data, boton_BlockUp, 3)
                    dis.blit(font50.render("->", True, colorBlock.data), (botonx+260, 307))

                    boton_BlockD_S = pygame.Rect(botonx-100, 310, 50, 50)
                    boton_BlockD = pygame.Rect(botonx-110, 300, 50, 50)
                    pygame.draw.rect(dis, white_S, boton_BlockD_S, 10)
                    pygame.draw.rect(dis, black, boton_BlockD)
                    pygame.draw.rect(dis, colorBlock.data, boton_BlockD, 3)
                    dis.blit(font50.render("<-", True, colorBlock.data), (botonx-100, 307))

                    if boton_atras.collidepoint((mx, my)):
                        if click:
                            running = False
                    if boton_UpV.collidepoint((mx, my)):
                        if click:
                            if volumen < 100:
                                Vol.play()
                                volumen += 10
                                ajustar_volumen(volumen / 100.0)
                    if boton_DnV.collidepoint((mx, my)):
                        if click:
                            if volumen > 0:
                                Vol.play()
                                volumen -= 10
                                ajustar_volumen(volumen / 100.0)
                    if boton_UpC.collidepoint((mx, my)):
                        if click:
                            Vol.play()
                            # FIXME: En la última posición de la lista se rompe al avanzar.
                            colorSk = colorSk.next
                    if boton_DnC.collidepoint((mx, my)):
                        if click:
                            Vol.play()
                            # FIXME: En la primera posición de la lista se rompe al retroceder.
                            colorSk = colorSk.prev
                    if boton_BlockUp.collidepoint((mx, my)):
                        if click:
                            Vol.play()
                            # FIXME: En la última posición de la lista se rompe al avanzar.
                            colorBlock = colorBlock.next
                    if boton_BlockD.collidepoint((mx, my)):
                        if click:
                            Vol.play()
                            # FIXME: En la primera posición de la lista se rompe al retroceder.
                            colorBlock = colorBlock.prev
                    click = False
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            #sys.exit()
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                running = False
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True
                    
                    pygame.display.update()
                    mainClock.tick(60)
        elif boton_3.collidepoint((mx, my)):
            if click:
                GameSel.play()
                running = True
                while running:
                    dis.fill((black))
                    draw_text('Creditos', font, white, dis, 100, 20)
                    # Datos 
                    creditosF = open('./PROYECTO/Viable/S_N_A_K_E/Creditos.txt', 'rt', encoding = 'utf-8')
                    draw_text(creditosF.readline(), score_font, white, dis, 100, 100)
                    draw_text(creditosF.readline(), score_font, white, dis, 100, 200)
                    draw_text(creditosF.readline(), score_font, white, dis, 100, 300)
                    draw_text(creditosF.readline(), score_font, white, dis, 100, 400)
                    draw_text(creditosF.readline(), score_font, white, dis, 100, 500)

                    # Boton
                    mx, my = pygame.mouse.get_pos()
                    boton_atras_S = pygame.Rect(30, 20, 50, 50)
                    boton_atras = pygame.Rect(25, 15, 50, 50)
                    pygame.draw.rect(dis, white_S, boton_atras_S, 10)
                    pygame.draw.rect(dis, black, boton_atras)
                    pygame.draw.rect(dis, white, boton_atras, 3)
                    dis.blit(font.render("<-", True, white), (30, 19))
                    if boton_atras.collidepoint((mx, my)):
                        if click:
                            running = False
                    click = False
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            #sys.exit()
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                running = False
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True
                    
                    pygame.display.update()
                    mainClock.tick(60)
                    creditosF.close()
        elif boton_4.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(dis, green_S, boton_1S, 10)
        pygame.draw.rect(dis, black, boton_1)
        pygame.draw.rect(dis, green, boton_1, 3)
        dis.blit(font_style.render("Iniciar juego", True, (255, 255, 255)), (botonx+55, 116))
        pygame.draw.rect(dis, blue_S, boton_2S, 10)
        pygame.draw.rect(dis, black, boton_2)
        pygame.draw.rect(dis, blue, boton_2, 3)
        dis.blit(font_style.render("Opciones", True, (255, 255, 255)), (botonx+65, 216))
        pygame.draw.rect(dis, yellow_S, boton_3S, 10)
        pygame.draw.rect(dis, black, boton_3)
        pygame.draw.rect(dis, yellow, boton_3, 3)
        dis.blit(font_style.render("Creditos", True, (255, 255, 255)), (botonx+65, 316))
        pygame.draw.rect(dis, red_S, boton_4S, 10)
        pygame.draw.rect(dis, black, boton_4)
        pygame.draw.rect(dis, red, boton_4, 3)
        dis.blit(font_style.render("Salir del juego", True, (255, 255, 255)), (botonx+45, 416))
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)

# Es el llamado a la primera función que se ejecutará
main_menu()