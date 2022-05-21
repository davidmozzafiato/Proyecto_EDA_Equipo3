# Bibliotecas requeridas ----------------------------------------------------------------- #
import pygame, sys, random, time
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
# Definición de colores para un rápido uso ----------------------------------------------- #
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
rojo_que_no_parece_red = (213, 50, 80)
rojo_no_tan_red = (100, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)
clock = pygame.time.Clock()
# Velocidad de nuestro poderoso snake ---------------------------------------------------- #
snake_block = 10
snake_speed = 15
#Tipografías a usar ---------------------------------------------------------------------- #
font = pygame.font.SysFont("bahnschrift", 60)
font50 = pygame.font.SysFont("bahnschrift", 50)
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 35)
# Inicializamos el click ----------------------------------------------------------------- #
click = False
# Importamos los sonidos
GameSel = pygame.mixer.Sound("./Sonidos/GameSel.mp3")
AppleBite = pygame.mixer.Sound("./Sonidos/AppleBite.mp3")
Snakeeeeee = pygame.mixer.Sound("./Sonidos/Snakeeeee.mp3")
Die = pygame.mixer.Sound("./Sonidos/mixkit-retro-arcade-game-over-470.wav")
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
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
# Otra forma de imprimir en pantalla
def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / x, dis_height / y])
# Menú principal
def main_menu():
    while True:
        dis.fill((black))
        draw_text('S N A K E E E E E E E E E E E E', font, white, dis, 100, 20)
        mx, my = pygame.mouse.get_pos()
        botonx = dis_center-100
        boton_1 = pygame.Rect(botonx, 100, 200, 50)
        boton_2 = pygame.Rect(botonx, 200, 200, 50)
        boton_3 = pygame.Rect(botonx, 300, 200, 50)
        boton_4 = pygame.Rect(botonx, 400, 200, 50)
        if boton_1.collidepoint((mx, my)):
            if click:
                GameSel.play()
                juego()
        if boton_2.collidepoint((mx, my)):
            if click:
                GameSel.play()
                opciones()
        if boton_3.collidepoint((mx, my)):
            if click:
                GameSel.play()
                creditos()
        if boton_4.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(dis, black, boton_1)
        pygame.draw.rect(dis, green, boton_1, 3)
        dis.blit(font_style.render("Iniciar juego", True, (255, 255, 255)), (botonx+55, 116))
        pygame.draw.rect(dis, black, boton_2)
        pygame.draw.rect(dis, blue, boton_2, 3)
        dis.blit(font_style.render("Opciones", True, (255, 255, 255)), (botonx+65, 216))
        pygame.draw.rect(dis, black, boton_3)
        pygame.draw.rect(dis, yellow, boton_3, 3)
        dis.blit(font_style.render("Creditos", True, (255, 255, 255)), (botonx+65, 316))
        pygame.draw.rect(dis, black, boton_4)
        pygame.draw.rect(dis, red, boton_4, 3)
        dis.blit(font_style.render("Salir del juego", True, (255, 255, 255)), (botonx+45, 416))
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                #sys.exit()
            # Función usada para salir del juego presionando ESC, pero se implementó un botón dedicado. ------------ # 
            '''if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()'''
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
score1 = 0
# Función que contiene el juego
def juego():
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
    # TODO: Reparar el poder entrar en el bucle "Jugar de nuevo" más de dos veces seguidas
    # click = False produce pantallazos luego de iteradas veces de morir
    while not game_over:
 
        while game_close == True:
            # TODO: Reparar el sonido de muerte
            # Die.play()
            dis.fill(rojo_no_tan_red)
            if score1 == range(0, 2):
                draw_text('Te moriste, pensé que durarías más ):', font50, white, dis, 100, 100)
            if score == range(3, 5):
                draw_text('Kpro', font50, white, dis, 100, 100)
            mx, my = pygame.mouse.get_pos()
            botonx = dis_center-100
            boton_1 = pygame.Rect(botonx, 250, 200, 50)
            boton_2 = pygame.Rect(botonx, 350, 200, 50)
            pygame.draw.rect(dis, black, boton_1)
            pygame.draw.rect(dis, green, boton_1, 3)
            dis.blit(font_style.render("Jugar de nuevo", True, white), (botonx+40, 266))
            pygame.draw.rect(dis, black, boton_2)
            pygame.draw.rect(dis, red, boton_2, 3)
            dis.blit(font_style.render("Menú principal", True, white), (botonx+45, 366))
            if boton_1.collidepoint((mx, my)):
                if click:
                    GameSel.play()
                    juego()
            if boton_2.collidepoint((mx, my)):
                if click:
                    GameSel.play()
                    game_over = True
                    game_close = False
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    #sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        game_over = True
                        game_close = False
                    if event.key == K_c:
                        juego()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            score1 = Length_of_snake - 1
            Your_score(Length_of_snake - 1)
            print("score1: " + str(score1))
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
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
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
# Menú de opciones falta pensar que opcines implementar, jajaja
def opciones():
    running = True
    while running:
        dis.fill((black))
        draw_text('Opciones', font, white, dis, 100, 20)
        mx, my = pygame.mouse.get_pos()
        boton_atras = pygame.Rect(25, 15, 50, 50)
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
# Aquí van los datos de las personas involucradas en la creación del juego
def creditos():
    running = True
    while running:
        dis.fill((black))
        draw_text('Creditos', font, white, dis, 100, 20)
        # Datos 
        draw_text('Ideas: David Pinto', score_font, white, dis, 100, 100)
        draw_text('Diseño: David Pinto', score_font, white, dis, 100, 200)
        draw_text('Snake: David Pinto', score_font, white, dis, 100, 300)
        draw_text('Menús: David Pinto', score_font, white, dis, 100, 400)
        draw_text('Supervisor de la obra: El yizus Dp', score_font, white, dis, 100, 500)

        # Boton
        mx, my = pygame.mouse.get_pos()
        boton_atras = pygame.Rect(25, 15, 50, 50)
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
# Es el llamado a la primera función que se ejecutará
main_menu()