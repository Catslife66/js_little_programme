import pygame
import pygame.font
import random

screen_width = 600
screen_height = 600
running = True
white = (255, 255, 255)
bg_colour = (50, 25, 50)
paddle_width = 20
paddle_height = 80
border = 60
paddle1_x = 0
paddle1_y = (screen_height + border) / 2 - paddle_height / 2
paddle2_x = screen_width - paddle_width
paddle2_y = (screen_height + border) / 2- paddle_height / 2
ball_centerx = screen_width / 2
ball_centery = (screen_height + border) / 2
radius = 10
score1 = 0
score2 = 0
winning = False
clock = pygame.time.Clock()



pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')


class Paddle():
    def __init__(self, x, y):
        self.speed = 5
        self.rect = pygame.Rect(0, 0, paddle_width, paddle_height)
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y

    def player1_move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > border:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < screen_height:
            self.rect.y += self.speed

    def player2_move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > border:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < screen_height:
            self.rect.y += self.speed

    def draw_paddle(self):
        pygame.draw.rect(screen, white, self.rect)


class Ball():
    def __init__(self):
        self.rect = pygame.Rect(0, 0, radius, radius)
        self.rect.top = ball_centery - radius
        self.rect.bottom = ball_centery + radius
        self.rect.right = ball_centerx + radius
        self.rect.left = ball_centerx - radius
        self.speed = 3
        self.x_direction = random.choice([-1, 1])
        self.y_direction = random.choice([-1, 1])
        self.winner = 0

    def move(self):
        if self.rect.top < border:
            self.y_direction *= -1
        if self.rect.bottom > screen_height:
            self.y_direction *= -1

        if self.rect.colliderect(paddle1.rect):
            self.x_direction *= -1
            self.speed += 1
        if self.rect.colliderect(paddle2.rect):
            self.x_direction *= -1
            self.speed += 1
            
        self.rect.x += self.speed * self.x_direction
        self.rect.y += self.speed * self.y_direction

    def draw_ball(self):
        pygame.draw.circle(screen, white, (self.rect.right - radius, self.rect.top + radius), radius)


def show_text(txt):
    font = pygame.font.SysFont(None, 40)
    text_img = font.render(txt, True, white)
    text_img_rect = text_img.get_rect()
    text_img_rect.centerx = screen_width/2
    text_img_rect.centery = border/2
    screen.blit(text_img, text_img_rect)

paddle1 = Paddle(paddle1_x, paddle1_y)
paddle2 = Paddle(paddle2_x, paddle2_y)
ball = Ball()


while running:
    clock.tick(60)
    screen.fill(bg_colour)
    pygame.draw.line(screen, white, (0, border), (screen_width, border))
    paddle1.draw_paddle()
    paddle2.draw_paddle()
    ball.draw_ball()
    show_text(f"{score1} : {score2}")

    if not winning:
        paddle1.player1_move()
        paddle2.player2_move()
        ball.move()
        if ball.rect.right < 0:
            score2 += 1
            winning = True
        if ball.rect.left - 10 >= screen_width:
            score1 += 1
            winning = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and winning:
            ball = Ball()
            winning = False
            paddle1 = Paddle(paddle1_x, paddle1_y)
            paddle2 = Paddle(paddle2_x, paddle2_y)

    pygame.display.update()