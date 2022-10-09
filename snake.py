from tkinter import font
import pygame
import random
import pygame.font

pygame.init()

screen_width = 600
screen_height = 600
unitsize = 20
bg_colour = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
# 1 going up, 2 going down, 3 going left, 4 going right
direction = 0
score = 0
game_over = False

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('SNAKE GAME')

# snake head
head = pygame.Rect(0, 0, unitsize, unitsize)
head.centerx = screen_width/2
head.centery = screen_height/2

# snake bodies
snake = []
snake.append(head)
snake.append([head.x, head.y + unitsize])
snake.append([head.x, head.y + unitsize*2])

#create food
foods = []
food_x = random.randint(0, screen_width - unitsize)
food_y = random.randint(0, screen_height - unitsize)
food = pygame.Rect(food_x, food_y, unitsize, unitsize)
foods.append(food)

#show_score
def show_score(x, y):
    txt = f"Score: {score}"
    font = pygame.font.SysFont(None, 30)
    font_img = font.render(txt, True, white)
    screen.blit(font_img, (x, y))

def show_gameover():
    txt = "Game Over!"
    font = pygame.font.SysFont(None, 60)
    font_img = font.render(txt, True, white)
    font_rect = font_img.get_rect()
    font_rect.centerx = screen_width / 2
    font_rect.centery = screen_height / 2
    screen.blit(font_img, font_rect)

def draw_replay_button():
    txt = "Restart"
    font = pygame.font.SysFont(None, 45)
    font_img = font.render(txt, True, bg_colour)
    restart_rect = pygame.Rect(0, 0, 140, 40)
    restart_rect.centerx = screen_width / 2
    restart_rect.centery = screen_height / 2 + 100
    font_rect = font_img.get_rect()
    font_rect.center = restart_rect.center
    pygame.draw.rect(screen, white, restart_rect)
    screen.blit(font_img, font_rect)

    
# Restart button
restart_rect = pygame.Rect(0, 0, 140, 40)
restart_rect.centerx = screen_width / 2
restart_rect.centery = screen_height / 2 + 100

def reset_game():
    screen.fill(bg_colour)
    head = pygame.Rect(0, 0, unitsize, unitsize)
    head.centerx = screen_width/2
    head.centery = screen_height/2
    snake = []
    snake.append(head)
    snake.append([head.x, head.y + unitsize])
    snake.append([head.x, head.y + unitsize*2])
    food_x = random.randint(0, screen_width - unitsize)
    food_y = random.randint(0, screen_height - unitsize)
    food = pygame.Rect(food_x, food_y, unitsize, unitsize)
    foods.append(food)


running = True
clock = pygame.time.Clock()

while running:
    clock.tick(10)
    screen.fill(bg_colour)
    show_score(0, 0)
            
    if not game_over:
        # move snake
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != 2:
            direction = 1
        elif keys[pygame.K_DOWN] and direction != 1:
            direction = 2
        elif keys[pygame.K_LEFT] and direction != 4:
            direction = 3
        elif keys[pygame.K_RIGHT] and direction != 3:
            direction = 4

        if direction == 1:
            snake.pop()
            snake.insert(0, (snake[0][0], snake[0][1]-unitsize, unitsize, unitsize))
        if direction == 2:
            snake.pop()
            snake.insert(0, (snake[0][0], snake[0][1]+unitsize, unitsize, unitsize))
        if direction == 3:
            snake.pop()
            snake.insert(0, (snake[0][0] - unitsize, snake[0][1], unitsize, unitsize))
        if direction == 4:
            snake.pop()
            snake.insert(0, (snake[0][0] + unitsize, snake[0][1], unitsize, unitsize))

    # collide border
    if snake[0][0] <= 0 or snake[0][0] >= screen_width - unitsize:
        game_over = True    
    if snake[0][1] <= 0 or snake[0][1] >= screen_height - unitsize:
        game_over = True
    # collide body  
    for i in range(1, len(snake)):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True

    if game_over:
        show_gameover()
        draw_replay_button()
        

    # eat food
    head_rect = pygame.Rect(snake[0][0], snake[0][1], unitsize, unitsize)
    if head_rect.colliderect(food):
        score += 1
        snake.append(food)
        foods.pop()
        food_x = random.randint(0, screen_width - unitsize)
        food_y = random.randint(0, screen_height - unitsize)
        food = pygame.Rect(food_x, food_y, unitsize, unitsize)
        foods.append(food)

    # draw food
    for item in foods:
        pygame.draw.rect(screen, green, item)

    # draw snake
    pygame.draw.rect(screen, red, (snake[0][0], snake[0][1], unitsize, unitsize))
    for i in range(1, len(snake), 1):
        pygame.draw.rect(screen, blue, (snake[i][0], snake[i][1], unitsize, unitsize))

    # detect game event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            pos = pygame.mouse.get_pos()
            if restart_rect.collidepoint(pos):
                game_over = False
                screen.fill(bg_colour)
                score = 0
                head = pygame.Rect(0, 0, unitsize, unitsize)
                head.centerx = screen_width/2
                head.centery = screen_height/2
                snake = []
                snake.append(head)
                snake.append([head.x, head.y + unitsize])
                snake.append([head.x, head.y + unitsize*2])
                foods.pop()
                food = pygame.Rect(food_x, food_y, unitsize, unitsize)
                foods.append(food)

    # update screen
    pygame.display.update()
