import pygame
import math


def round_up_to_1000(number):
    return math.ceil(number / 1000) * 1000


def round_down_to_1000(number):
    return math.floor(number / 1000) * 1000


time = pygame.time.Clock()

# Инициализация игры  
pygame.init()
screen = pygame.display.set_mode((1000, 600))  # разрешение экрана
pygame.display.set_caption("Maverick")  # Имя приложения  
# icon = pygame.image.load('images/Maverick.ico')
# pygame.display.set_icon(icon)
master_music = pygame.mixer.Sound('resource/sound/Into_Eternity.mp3')  # Мелодия
master_music.play()
bg = pygame.image.load('resource/BG.jpeg')
player_stay = pygame.image.load('resource/person/walk_right/person_1.png')

player_walk_right = [

    pygame.image.load('resource/person/walk_right/person_3.png'),
    pygame.image.load('resource/person/walk_right/person_2.png'),
    pygame.image.load('resource/person/walk_right/person_2.png'),
    pygame.image.load('resource/person/walk_right/person_1.png'),
    pygame.image.load('resource/person/walk_right/person_1.png'),
    pygame.image.load('resource/person/walk_right/person_2.png'),
    pygame.image.load('resource/person/walk_right/person_2.png'),
    pygame.image.load('resource/person/walk_right/person_3.png'),
    pygame.image.load('resource/person/walk_right/person_3.png'),
    pygame.image.load('resource/person/walk_right/person_4.png'),
    pygame.image.load('resource/person/walk_right/person_4.png'),
    pygame.image.load('resource/person/walk_right/person_5.png'),
    pygame.image.load('resource/person/walk_right/person_5.png'),
    pygame.image.load('resource/person/walk_right/person_4.png'),
    pygame.image.load('resource/person/walk_right/person_4.png'),
    pygame.image.load('resource/person/walk_right/person_3.png'),

]

player_walk_left = [

    pygame.image.load('resource/person/walk_left/person_3.png'),
    pygame.image.load('resource/person/walk_left/person_2.png'),
    pygame.image.load('resource/person/walk_left/person_2.png'),
    pygame.image.load('resource/person/walk_left/person_1.png'),
    pygame.image.load('resource/person/walk_left/person_1.png'),
    pygame.image.load('resource/person/walk_left/person_2.png'),
    pygame.image.load('resource/person/walk_left/person_2.png'),
    pygame.image.load('resource/person/walk_left/person_3.png'),
    pygame.image.load('resource/person/walk_left/person_3.png'),
    pygame.image.load('resource/person/walk_left/person_4.png'),
    pygame.image.load('resource/person/walk_left/person_4.png'),
    pygame.image.load('resource/person/walk_left/person_5.png'),
    pygame.image.load('resource/person/walk_left/person_5.png'),
    pygame.image.load('resource/person/walk_left/person_4.png'),
    pygame.image.load('resource/person/walk_left/person_4.png'),
    pygame.image.load('resource/person/walk_left/person_3.png'),

]
player_walk = 0
player_speed = 30
player_x = 200
player_y = 250

bg_x = 0
game = True
while game:
    time.tick(20)
    ''' Задний фон'''
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x - 1000, 0))  # движение второго задника
    screen.blit(bg, (bg_x + 1000, 0))  # движение второго задника

    ''' Персонаж и анимация'''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:  # Влево
        bg_x += 7

        screen.blit(player_walk_left[player_walk], (player_x, player_y))
        player_walk += 1
        if player_walk == 16:
            player_walk = 0

    elif keys[pygame.K_d]:  # Вправо
        bg_x -= 7

        screen.blit(player_walk_right[player_walk], (player_x, player_y))
        player_walk += 1
        if player_walk == 16:
            player_walk = 0

    elif keys[pygame.K_SPACE]:
        screen.blit(player_stay, (300, 230))
        screen.blit(player_stay, (300, 210))
        screen.blit(player_stay, (300, 180))
        screen.blit(player_stay, (300, 210))
        screen.blit(player_stay, (300, 230))

    else:
        screen.blit(player_stay, (player_x, player_y))

    if bg_x >= 1000 or bg_x <= -1000:
        bg_x = 0

    ''' Экран '''
    pygame.display.update()  # Обновление экрана

    ''' Работа с событиями'''
    # Выход из игры
    for event in pygame.event.get():  # Получение списка событий
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()  # Выход из приложения

    ''' Прочее '''
