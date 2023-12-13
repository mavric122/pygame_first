import pygame
import random

time = pygame.time.Clock()

# Инициализация игры  
pygame.init()
screen = pygame.display.set_mode((1000, 600))  # разрешение экрана
pygame.display.set_caption("Maverick")  # Имя приложения  
# icon = pygame.image.load('images/Maverick.ico')
# pygame.display.set_icon(icon)

master_music = pygame.mixer.Sound('resource/sound/Into_Eternity.mp3')  # Мелодия
master_music.play()

# Объекты
bg = pygame.image.load('resource/BG.jpeg').convert()
player_stay = pygame.image.load('resource/person/walk_right/person_1.png').convert_alpha()
enemy_1 = pygame.image.load('resource/enemy/enemy_test.png').convert_alpha()

rand = random.randint(2000, 6000)
enemy_1_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_1_timer, rand)
enemy_list_in_game = []

# Анимации
player_walk_right = [
    pygame.image.load('resource/person/walk_right/person_3.png').convert_alpha(),
    pygame.image.load('resource/person/walk_right/person_2.png').convert_alpha(),
    pygame.image.load('resource/person/walk_right/person_2.png').convert_alpha(),
    pygame.image.load('resource/person/walk_right/person_1.png').convert_alpha(),
    pygame.image.load('resource/person/walk_right/person_1.png').convert_alpha(),
    pygame.image.load('resource/person/walk_right/person_2.png').convert_alpha(),
    pygame.image.load('resource/person/walk_right/person_2.png').convert_alpha(),
    pygame.image.load('resource/person/walk_right/person_3.png').convert_alpha(),
    pygame.image.load('resource/person/walk_right/person_3.png').convert_alpha(),
    pygame.image.load('resource/person/walk_right/person_4.png').convert_alpha(),
    pygame.image.load('resource/person/walk_right/person_4.png').convert_alpha(),
    pygame.image.load('resource/person/walk_right/person_5.png').convert_alpha(),
    pygame.image.load('resource/person/walk_right/person_5.png').convert_alpha(),
    pygame.image.load('resource/person/walk_right/person_4.png').convert_alpha(),
    pygame.image.load('resource/person/walk_right/person_4.png').convert_alpha(),
    pygame.image.load('resource/person/walk_right/person_3.png').convert_alpha(),
]
player_walk_left = [

    pygame.image.load('resource/person/walk_left/person_3.png').convert_alpha(),
    pygame.image.load('resource/person/walk_left/person_2.png').convert_alpha(),
    pygame.image.load('resource/person/walk_left/person_2.png').convert_alpha(),
    pygame.image.load('resource/person/walk_left/person_1.png').convert_alpha(),
    pygame.image.load('resource/person/walk_left/person_1.png').convert_alpha(),
    pygame.image.load('resource/person/walk_left/person_2.png').convert_alpha(),
    pygame.image.load('resource/person/walk_left/person_2.png').convert_alpha(),
    pygame.image.load('resource/person/walk_left/person_3.png').convert_alpha(),
    pygame.image.load('resource/person/walk_left/person_3.png').convert_alpha(),
    pygame.image.load('resource/person/walk_left/person_4.png').convert_alpha(),
    pygame.image.load('resource/person/walk_left/person_4.png').convert_alpha(),
    pygame.image.load('resource/person/walk_left/person_5.png').convert_alpha(),
    pygame.image.load('resource/person/walk_left/person_5.png').convert_alpha(),
    pygame.image.load('resource/person/walk_left/person_4.png').convert_alpha(),
    pygame.image.load('resource/person/walk_left/person_4.png').convert_alpha(),
    pygame.image.load('resource/person/walk_left/person_3.png').convert_alpha(),

]

# Игровые переменные
player_walk = 0
player_speed = 30
player_x = 200
player_y = 250
is_jump = False  # Прыжок
just_count = 9  # Высота прыжка
bg_x = 0
enemy_1_x = 1300
enemy_1_y = 380

game = True
while game:
    time.tick(20)

    ''' Задний фон'''
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x - 1000, 0))  # движение второго задника
    screen.blit(bg, (bg_x + 1000, 0))  # движение второго задника

    ''' Персонаж и анимация'''
    player_rect = player_walk_left[0].get_rect(topleft=(player_x, player_y))  # Красный квадрат игрока для отслеживания

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

    else:
        screen.blit(player_stay, (player_x, player_y))
    # Прыжок
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if just_count >= -9:
            if just_count > 0:
                player_y -= (just_count ** 2) / 2
            else:
                player_y += (just_count ** 2) / 2
            just_count -= 1
        else:
            is_jump = False
            just_count = 9

    if bg_x >= 1000 or bg_x <= -1000:
        bg_x = 0

    '''Враги'''
    enemy_1_rect = enemy_1.get_rect(topleft=(enemy_1_x, 380))

    if enemy_list_in_game:
        for enemy_rect in enemy_list_in_game:
            screen.blit(enemy_1, enemy_rect.topleft)
            enemy_rect.x -= 20  # Изменение координаты x

        # Проверка на столкновение игрока с врагом
        for enemy_rect in enemy_list_in_game:
            if player_rect.colliderect(enemy_rect):
                print("Проиграл!")

    ''' Экран '''
    pygame.display.update()  # Обновление экрана

    ''' Работа с событиями'''
    # Выход из игры
    for event in pygame.event.get():  # Получение списка событий
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()  # Выход из приложения
        if event.type == enemy_1_timer:
            enemy_list_in_game.append(enemy_1.get_rect(topleft=(enemy_1_x, enemy_1_y)))

    ''' Прочее '''
