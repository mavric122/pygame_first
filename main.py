import pygame

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
player_stay = pygame.image.load('resource/person/walk_left/person_1.png')
player_walk_right = [
    pygame.image.load('resource/person/walk_left/person_3.png'),
    pygame.image.load('resource/person/walk_left/person_2.png'),
    pygame.image.load('resource/person/walk_left/person_1.png'),
    pygame.image.load('resource/person/walk_left/person_2.png'),
    pygame.image.load('resource/person/walk_left/person_3.png'),
    pygame.image.load('resource/person/walk_left/person_4.png'),
    pygame.image.load('resource/person/walk_left/person_5.png'),
    pygame.image.load('resource/person/walk_left/person_4.png'),
    pygame.image.load('resource/person/walk_left/person_3.png'),
]
player_walk = 0
player_speed = 30
player_x = 120

bg_x = 0
screen_walk = 0 # Счётчик пройденных экранов
game = True
while game:
    time.tick(5)
    ''' Задний фон'''
    screen.blit(bg, (bg_x, 0))
    # screen.blit(bg, (bg_x + 1000, 0))
    # bg_x -= 10  # движение второго задника
    # if bg_x <= -1000:
    #     bg_x = 0
    #     screen_walk += 1
    # if screen_walk == 3:
    #     print("End Level!")
    #     game = False

    ''' Персонаж и анимация'''
    player_walk += 1
    if player_walk == 9:
        player_walk = 0


    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        screen.blit(player_walk_right[player_walk], (player_x, 250))
        player_x -= player_speed
    elif keys[pygame.K_d]:
        screen.blit(player_walk_right[player_walk], (player_x, 250))
        player_x += player_speed
    else:
        screen.blit(player_stay, (player_x, 250))

    ''' Работа с событиями'''
    # Выход из игры
    for event in pygame.event.get():  # Получение списка событий
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()  # Выход из приложения

    ''' Экран '''
    pygame.display.update()  # Обновление экрана

    ''' Прочее '''

