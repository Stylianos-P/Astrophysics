import pygame as pg
import math
import random
pg.init()

screen_width = 1400
screen_height = (screen_width // 2)
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('3D Projection')
clock = pg.time.Clock()
fps = 60
scale = 100
theta = 0
# COLOURS
black = (0, 0, 0)
white = (255, 255, 255)
grey = (200, 200, 200)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

class gravity:
    def __init__(self,x,y,strength,color):
        self.x = x
        self.y = y
        self.strength = strength
        self.color = color
    def draw(self,surface):
        pg.draw.circle(surface,self.color,(self.x,self.y),5)

class particle:
    def __init__(self,x,y,color,vx,vy):
        self.x = x
        self.y =y
        self.color = color
        self.vx = vx
        self.vy = vy

    def move(self,g):
        dist_x = g.x - self.x
        dist_y = g.y - self.y
        dist = ((dist_x ** 2) + (dist_y ** 2)) ** 0.5
        inversedist = 1/dist
        normalised_x = inversedist*dist_x
        normalised_y = inversedist*dist_y

        inverse_square_dropoff = inversedist*inversedist

        acceleration_x = normalised_x*g.strength*inverse_square_dropoff
        acceleration_y= normalised_y*g.strength*inverse_square_dropoff

        self.vx += acceleration_x
        self.vy += acceleration_y

        self.x += self.vx
        self.y += self.vy
       #if 0<self.x<screen_width:
       #    self.vx = self.vx
       #else:
       #    self.vx = -self.vx
       #if 0<self.y<screen_height:
       #    self.vy = self.vy
       #else:
       #    self.vy = -self.vy




    def draw(self,surface):
        pg.draw.circle(surface,self.color,(self.x,self.y),1)

g = gravity(screen_width/2,screen_height/2,1000,yellow)
#g2 = gravity(screen_width/2-400,screen_height/2,1000,yellow)
#p = particle(screen_width/2,200,white,2.8,0)

particles = []
for i in range(1, 10001):
    p = particle(screen_width/2+random.randint(-50,50),random.randint(0,100)+100,(random.randint(150,255),random.randint(150,255),random.randint(150,255)),2,0)
    particles.append(p)

run = True
while run:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    screen.fill(black)
    for i in particles:
        i.draw(screen)
        i.move(g)
#        i.move(g2)


    g.draw(screen)
    #g2.draw(screen)


    pg.display.update()

