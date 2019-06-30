import pygame
import random
import time
import os


running = True
FPS = 30

#Colors
BLACK = (0, 0,  0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#Background
background_color = (255, 255, 255)
screen_width = 800
screen_height = 800

#Other Stuff
difficulty = "Normal"
mode = "arrow"
state = "Start"
direction = "Up"
Chara = "CharaU.png"
Start = 0
shieldx = 382
shieldy = 380
b = 36
l = 3
GO = 0
t = 0
r = 0
v = 0
q = 0
p = 0
looper = 0
LOOP = 0
remove = 0
time = 0
velocity = 10
health = 3
yes = None

#Spear Coordinates
spear1_x = 802
spear1_y = 400

spear2_x = -65
spear2_y = 400

spear3_x = 400
spear3_y = -65

spear4_x = 400
spear4_y = 830

#Initialize
pygame.init()
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Test')
clock = pygame.time.Clock()

#Text Sizes
#textfont = pygame.font.SysFont(None, 30)
tinyfont = pygame.font.SysFont(None, 30)
timerfont = pygame.font.SysFont(None, 60)
bigfont = pygame.font.SysFont(None, 120)

#Folder Finder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "SpritesP")

#Background Maker
background = pygame.image.load(os.path.join(img_folder, "Grass.jpg")).convert()
background_rect = background.get_rect()

#Heart Maker
heart1 = pygame.image.load(os.path.join(img_folder, "Heart.png")).convert()
heart1_rect = heart1.get_rect()
heart1_rect.center = (20, 30)
heart1.set_colorkey(WHITE)

heart2 = pygame.image.load(os.path.join(img_folder, "Heart.png")).convert()
heart2_rect = heart2.get_rect()
heart2_rect.center = (55, 30)
heart2.set_colorkey(WHITE)

heart3 = pygame.image.load(os.path.join(img_folder, "Heart.png")).convert()
heart3_rect = heart3.get_rect()
heart3_rect.center = (90, 30)
heart3.set_colorkey(WHITE)

#Sprites
class PlayerP(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, Chara)).convert()
        self.image.set_colorkey(WHITE)
        #self.image = pygame.Surface((20,20))
        #self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 400)

#Right
class Spear1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "SpearR.png")).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (spear1_x, spear1_y)

    def update(self):
        self.rect.x -= velocity
        
def Spear_Right():
    spear01 = Spear1()
    spears.add(spear01)

#Left        
class Spear2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "SpearL.png")).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (spear2_x, spear2_y)

    def update(self):
        if GO >= 3:
            self.rect.x += velocity

def Spear_Left():
    spear02 = Spear2()
    spears.add(spear02)
    
#Up
class Spear3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "SpearU.png")).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (spear3_x, spear3_y)

    def update(self):
        if GO >= 1:
            self.rect.y += velocity

def Spear_Up():
    spear03 = Spear3()
    spears.add(spear03)
    
#Down
class Spear4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "SpearD.png")).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (spear4_x, spear4_y)

    def update(self):
        if GO >= 2:
            self.rect.y -= velocity

def Spear_Down():
    spear04 = Spear4()
    spears.add(spear04)        

class Shield(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((b, l))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = (shieldx, shieldy)
   

#Groups
all_sprites = pygame.sprite.Group()
spears = pygame.sprite.Group()

#Sprites
spear01 = Spear1()
spears.add(spear01)

spear02 = Spear2()
spears.add(spear02)

spear03 = Spear3()
spears.add(spear03)

spear04 = Spear4()
spears.add(spear04)

shield = Shield()
all_sprites.add(shield)

playerP = PlayerP()
all_sprites.add(playerP)


#Timer
seconds = 60
second = 0


#The Actual Game
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       
            running = False 

    keyState = pygame.key.get_pressed()
    if keyState[pygame.K_ESCAPE]:
        running = False

    #Start Screen
    if state == "Start":
        screen.fill(background_color)

        spear01.kill()
        spear02.kill()
        spear03.kill()
        spear04.kill()

        spear01.kill()
        spear02.kill()
        spear03.kill()
        spear04.kill()
        

        
        pygame.sprite.Sprite.kill(spear01)
        pygame.sprite.Sprite.kill(spear02)
        pygame.sprite.Sprite.kill(spear03)
        pygame.sprite.Sprite.kill(spear04) 


        spear01 = Spear1()
        spears.add(spear01)

        spear02 = Spear2()
        spears.add(spear02)

        spear03 = Spear3()
        spears.add(spear03)

        spear04 = Spear4()
        spears.add(spear04)
        
             

        #Easter Eggs
        if keyState[pygame.K_LCTRL]:
            mode = "wasd"

        if keyState[pygame.K_LSHIFT]:
            mode = "arrow"

        if keyState[pygame.K_LALT]:
            difficulty = "Normal"

        if keyState[pygame.K_RALT]:
            difficulty = "Hard"

        #Difficulty
        if difficulty == "Normal":
            text = timerfont.render("Press space to start", True, (BLACK))
            textrect = text.get_rect()
            textrect.centerx = (screen_width / 2)
            textrect.centery = (screen_height / 2)

            if mode == "arrow":
                text2 = tinyfont.render("Use the arrow keys to block the projectiles", True, (BLACK))
                text2rect = text2.get_rect()
                text2rect.centerx = (screen_width / 2)
                text2rect.centery = (screen_height / 2) + 70

            if mode == "wasd":
                text2 = tinyfont.render("Use the wasd keys to block the projectiles", True, (BLACK))
                text2rect = text2.get_rect()
                text2rect.centerx = (screen_width / 2)
                text2rect.centery = (screen_height / 2) + 70

        if difficulty == "Hard":
            text = timerfont.render("Press space to start", True, (RED))
            textrect = text.get_rect()
            textrect.centerx = (screen_width / 2)
            textrect.centery = (screen_height / 2)

            if mode == "arrow":
                text2 = tinyfont.render("Use the arrow keys to block the projectiles", True, (RED))
                text2rect = text2.get_rect()
                text2rect.centerx = (screen_width / 2)
                text2rect.centery = (screen_height / 2) + 70

            if mode == "wasd":
                text2 = tinyfont.render("Use the wasd keys to block the projectiles", True, (RED))
                text2rect = text2.get_rect()
                text2rect.centerx = (screen_width / 2)
                text2rect.centery = (screen_height / 2) + 70

        screen.blit(text2, text2rect)

        if keyState[pygame.K_SPACE]:
            state = "Play"
    
    #Play Mode
    if state == "Play":

        screen.blit(background, background_rect)
       

        #Timer
        second = second + 1
        if second == 30:
            second = 0
            seconds = seconds - 1

    
        #Health
        if health >= 3:
            screen.blit(heart1, heart1_rect)
            screen.blit(heart2, heart2_rect)
            screen.blit(heart3, heart3_rect)

        if health == 2:
            screen.blit(heart1, heart1_rect)
            screen.blit(heart2, heart2_rect)

        if health == 1:
            screen.blit(heart1, heart1_rect)

        if health <= 0:
            velocity = 1000
            remove = remove + 1
            if remove == 3:
                velocity = 4
                remove = 0
                state = "Game over"

        #Controls
        if mode == "wasd":
            if keyState[pygame.K_a]:
                shield.kill()
                shieldx = 380
                shieldy = 382
                b = 3
                l = 36
                Chara = "CharaL.png"
                shield = Shield()
                all_sprites.add(shield)

            if keyState[pygame.K_d]:
                shield.kill()
                shieldx = 417
                shieldy = 382
                b = 3
                l = 36
                Chara = "CharaD.png"
                shield = Shield()
                all_sprites.add(shield)
            
            if keyState[pygame.K_w]:
                shield.kill()
                shieldx = 382
                shieldy = 380
                b = 36
                l = 3
                Chara = "CharaU.png"
                shield = Shield()
                all_sprites.add(shield)
            
            if keyState[pygame.K_s]:
                shield.kill()
                shieldx = 382
                shieldy = 418
                b = 36
                l = 3
                Chara = "CharaR.png"
                shield = Shield()
                all_sprites.add(shield)

        if mode == "arrow":
            if keyState[pygame.K_LEFT]:
                shield.kill()
                shieldx = 380
                shieldy = 382
                b = 3
                l = 36
                Chara = "CharaL.png"
                shield = Shield()
                all_sprites.add(shield)
                playerP = PlayerP()
                all_sprites.add(playerP)

            if keyState[pygame.K_RIGHT]:
                shield.kill()
                shieldx = 417
                shieldy = 382
                b = 3
                l = 36
                Chara = "CharaR.png"
                shield = Shield()
                all_sprites.add(shield)
                playerP = PlayerP()
                all_sprites.add(playerP)
            
            if keyState[pygame.K_UP]:
                shield.kill()
                shieldx = 382
                shieldy = 380
                b = 36
                l = 3
                Chara = "CharaU.png"
                shield = Shield()
                all_sprites.add(shield)
                playerP = PlayerP()
                all_sprites.add(playerP)
            
            if keyState[pygame.K_DOWN]:
                shield.kill()
                shieldx = 382
                shieldy = 418
                b = 36
                l = 3
                Chara = "CharaD.png"
                shield = Shield()
                all_sprites.add(shield)
                playerP = PlayerP()
                all_sprites.add(playerP)

            

        #Timers
        v = v + 1
        t = t + 1
        
        #Normal Mode
        if difficulty == "Normal":
            if Start == 0:
                velocity = 10
            Start = 1
            if t == 1:
                GO = 0
            if t == 26:
                GO = 1
            if t == 51:
                GO = 2
            if t == 76:
                GO = 3

            if t > 100:
                looper = looper + 1
                if looper == 12:
                    q =  random.randrange(1,5)
                    if q == 1:
                        Spear_Left()
                    if q == 2:
                        Spear_Right()
                    if q == 3:
                        Spear_Up()
                    if q == 4:
                        Spear_Down()
                    looper = 0

           
           


            if velocity <= 10:
                if v >= 900:
                    velocity = velocity + 1
                    v = 0

            if velocity > 10:
                if v >= 300:
                    velocity = velocity + 1
                    v = 0
        #Hard Mode
        if difficulty == "Hard":
            if Start == 0:
                velocity = 10
            Start = 1
            if t < 10:
                GO = 0
            if t >= 10:
                GO = 1
            if t >= 20:
                GO = 2
            if t >= 30:
                GO = 3

            if velocity <= 10:
                if v >= 900:
                    velocity = velocity + 1
                    v = 0

            if velocity > 10:
                if v >= 300:
                    velocity = velocity + 1
                    v = 0

        if seconds == 0:
            velocity = 1000
            remove = remove + 1
            if remove == 3:
                velocity = 4
                remove = 0
                state = "Win"

        
        #Collision       
        stop = pygame.sprite.spritecollide(shield, spears, True)
        hit = pygame.sprite.spritecollide(playerP, spears, True)
        #Spear hits Shield
        if stop:
            if state == "Play":
                health = health
#                if q == 1:
#                    spear01 = Spear1()
#                    spears.add(spear01)
                    
                
            
#                    yes = 1
#                if q == 2:
#                    spear02 = Spear2()
#                    spears.add(spear02)
                
            
#                    yes = 2
#                if q == 3:
#                    spear03 = Spear3()
#                    spears.add(spear03)
                
            
#                    yes = 3
#                if q == 4:
#                    spear04 = Spear4()
#                    spears.add(spear04)
                
            
#                    yes = 4

        #Spear hits player        
        elif hit:
            if state == "Play":
                health = health - 1
#                r =  random.randrange(1,5)
#                if r == 1:
#                    spear01 = Spear1()
#                    spears.add(spear01)
#                
#                if r == 2:
#                    spear02 = Spear2()
#                    spears.add(spear02)
#                
#                if r == 3:
#                    spear03 = Spear3()
#                    spears.add(spear03)
#               
#               if r == 4:
#                   spear04 = Spear4()
#                   spears.add(spear04)
                
        #Timer Text
        text = timerfont.render(str(seconds), True, (BLACK))
        textrect = text.get_rect()
        textrect.centerx = 770
        textrect.centery = 30

        #Drawing
        spears.draw(screen)
        spears.update()
        all_sprites.update()
        all_sprites.draw(screen)
    
    #Game Over Screen
    if state == "Game over":
        text = bigfont.render("Game Over", True, (RED))
        textrect = text.get_rect()
        textrect.centerx = (screen_width / 2)
        textrect.centery = (screen_height / 2)

        text2 = timerfont.render(str(seconds), True, (BLACK))
        text2rect = text2.get_rect()
        text2rect.centerx = 770
        text2rect.centery = 30

        difficulty = "Normal"

        screen.blit(text2, text2rect)

        if keyState[pygame.K_r]:
            health = 3
            seconds = 60
            Start = 0
            t = 0
            v = 0
            state = "Start"
            

        text2 = tinyfont.render("Press r to restart", False, (RED))
        text2rect = text2.get_rect()
        text2rect.centerx = (screen_width / 2)
        text2rect.centery = (screen_height / 2) + 40

        screen.blit(text2, text2rect)

    #Win Screen
    if state == "Win":
        text = bigfont.render("You win!", True, (BLACK))
        textrect = text.get_rect()
        textrect.centerx = (screen_width / 2)
        textrect.centery = (screen_height / 2)

    screen.blit(text, textrect)


    pygame.display.flip()
    pygame.display.update()

pygame.quit()