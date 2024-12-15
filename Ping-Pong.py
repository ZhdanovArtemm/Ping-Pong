from pygame import *
from random import *





init()
window = display.set_mode((700, 500))
display.set_caption('Лабиринт')
background = transform.scale(image.load('top_view.jpeg'), (700, 500))


player_speed = 3.5
player1_x = 30
player1_y = 250
player2_x = 650
player2_y = 250
speed_x = 3
speed_y = 3
points_blue = 0
points_red = 0


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_size_x, player_size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_size_x, player_size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update1(self):#! управление левой ракеткой
        keys_pressed = key.get_pressed()


        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    
    def update2(self):#? управление правой ракеткой
        keys_pressed = key.get_pressed()
    
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

class BALL(GameSprite):
    def update(self):
        self.rect.y += self.speed

 



#* описание предметов в игре:
FPS = 240
racket1 = Player("Racket_red.png", player1_x, player1_y, player_speed, 40, 100)#! сдесь нужна картингка ракетки вместо pass
racket2 = Player("Racket_blue.png", player2_x, player2_y, player_speed, 40, 100)#? сдесь нужна картингка ракетки вместо pass
ball = BALL("ball.png", 350, 250, randint(2, 4), 50, 50 )

font1 = font.SysFont("Arial", 36)
win = font1.render("Победил Красный", 1, (255, 0, 0))
lose = font1.render("Победил Синий", 1, (0, 0, 255))
clock = time.Clock()
game = True
finish = False  
while game:
    if finish != True:
        window.blit(background, (0, 0))
        racket1.reset()
        racket2.reset()
        racket1.update1()
        racket2.update2()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        text_lose = font1.render("Красный: " + str(points_red), 1, (255, 255, 255))
        text_win = font1.render("Синий:" + str(points_blue), 1, (255, 255,255))
        window.blit(text_lose, (280, 35))
        window.blit(text_win, (300, 7))
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        if ball.rect.x > 650:
            ball.rect.x = 350
            ball.rect.y = 250
            points_red += 1
            speed_x *= -1
            print("Очки красного", points_red)

        if  ball.rect.x < 0:
            ball.rect.x = 350
            ball.rect.y = 250
            points_blue += 1
            speed_x *= -1
            print("Очки голубого", points_blue)
        
        if points_blue >= 5:
            finish = True
            window.blit(lose, (200, 200))
            print("Победил Голубой")
        if points_red >= 5:
            window.blit(win, (200, 200))
            finish = True
            print("Победил Красный")

    for e in event.get():
        if e.type == QUIT:
            game = False



                

    clock.tick(FPS)
    display.update()