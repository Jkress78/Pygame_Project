import os
from typing import Iterable, Union
import pygame
from pygame.sprite import AbstractGroup
import wall_library
import random
import enemy
import trainer_library
import attacks
import constants
import moving_ball

class construction():

    def load_img():
        images = []
        os.chdir('./img')

        next_image = pygame.image.load("NextButt.gif").convert_alpha()
        images.append(next_image)

        start_image = pygame.image.load("StartButt.png").convert_alpha()
        images.append(start_image)

        background_image = pygame.image.load("poppy.png").convert()
        images.append(background_image)

        ball_out_image = pygame.image.load("ball_background.png").convert()
        images.append(ball_out_image)

        victory_image = pygame.image.load("victory.jpg").convert()
        images.append(victory_image)

        death_image = pygame.image.load("death.gif").convert()
        images.append(death_image)

        bCount_image = pygame.image.load("ball.gif").convert()
        images.append(bCount_image)

        ball_silhouette = pygame.image.load("ballG.gif").convert()
        images.append(ball_silhouette)

        caterpie_image = pygame.image.load("Caterpie.gif").convert()
        images.append(caterpie_image)

        pidgey_image = pygame.image.load("pidg.gif").convert()
        images.append(pidgey_image)

        rat_image = pygame.image.load("Rat.gif").convert()
        images.append(rat_image)

        ralts_image = pygame.image.load("Ralts.gif").convert()
        images.append(ralts_image)

        poocheyana_image = pygame.image.load("Poocheyana.gif").convert()
        images.append(poocheyana_image)

        dratini_image = pygame.image.load("Dratini.gif").convert()
        images.append(dratini_image)

        drifloon_image = pygame.image.load("Drifloon.gif").convert()
        images.append(drifloon_image)

        caterpie_silhouette = pygame.image.load("Blackout_C.gif").convert()
        images.append(caterpie_silhouette)

        pidgey_silhouette = pygame.image.load("Blackout_P.gif").convert()
        images.append(pidgey_silhouette)

        rat_silhouette = pygame.image.load("Blackout_RT.gif").convert()
        images.append(rat_silhouette)

        ralts_silhouette = pygame.image.load("Blackout_R.gif").convert()
        images.append(ralts_silhouette)

        poocheyana_silhouette = pygame.image.load("Blackout_PO.gif").convert()
        images.append(poocheyana_silhouette)

        dratini_silhouette = pygame.image.load("Blackout_DR.gif").convert()
        images.append(dratini_silhouette)

        drifloon_silhouette = pygame.image.load("Blackout_D.gif").convert()
        images.append(drifloon_silhouette)

        os.chdir('../src')
        return images
    
    def load_SFX():
        os.chdir('../sfx')
        sounds = []

        throw = pygame.mixer.Sound("throw.ogg")
        sounds.append(throw)

        catch = pygame.mixer.Sound("ball - catch.ogg")
        sounds.append(catch)

        transition_sound = pygame.mixer.Sound("skip.ogg")
        sounds.append(transition_sound)

        victory_sound = pygame.mixer.Sound("victory.ogg")
        sounds.append(victory_sound)

        lose_sound = pygame.mixer.Sound("lose.ogg")
        sounds.append(lose_sound)

        game_noise = pygame.mixer.Sound("game_sound.ogg")
        sounds.append(game_noise)

        os.chdir('../src')
        return sounds
    
    def build_walls():
        walls = pygame.sprite.Group()
        #-- Left Wall --
        walls.add(wall_library.Wall(-10, 0, 10, 900))

        #-- Right Wall --
        walls.add(wall_library.Wall(1000, 0, 10, 900))

        return walls
    
    def build_enemy_list():
        random.seed(8796)
        ralts = enemy.Enemy(random.randint(5,400), random.randint(5,400), 5, 5, 'Poocheyana.gif', 26, 34, 1)
        poocheyana = enemy.Enemy(random.randint(5, 400), random.randint(5, 400), 5, 5, 'Poocheyana.gif', 26, 34, 5)
        drifloon = enemy.Enemy(random.randint(5, 400), random.randint(5, 400), -4, -2, 'Drifloon.gif', 28, 42, 4)
        dratini = enemy.Enemy(random.randint(5, 400), random.randint(5, 400), 4, 4, 'Dratini.gif',  32, 42, 6)
        rat = enemy.Enemy(random.randint(5, 400), random.randint(5, 400), 5, 6, 'Rat.gif', 34, 38, 2)
        caterpie = enemy.Enemy(random.randint(5, 400), random.randint(5, 400), 2, 2,  'Caterpie.gif', 32, 42, 0)
        pidgey = enemy.Enemy(random.randint(5, 400), random.randint(5, 400), -4, -5, 'pidg.gif', 34, 35, 3)
        
        enemy_group = pygame.sprite.Group(ralts, poocheyana, drifloon, dratini, rat, caterpie, pidgey)
        enemy_list = [caterpie, ralts, rat, pidgey, drifloon, poocheyana, dratini]

        return enemy_group, enemy_list
    
    def build_player(walls):
        trainer = trainer_library.TrainerSprite(walls)
        trainer.rect.x = 0
        trainer.rect.y = 530
        trainer_list = pygame.sprite.Group(trainer)
        

        return trainer, trainer_list
    
    def build_attack_list():
        leaf = attacks.AttackSprites(0)
        leaf2 = attacks.AttackSprites(0)
        crescent = attacks.AttackSprites(1)
        tornado = attacks.AttackSprites(2)
        tornado2 = attacks.AttackSprites(2)
        fire = attacks.AttackSprites(3)
        pulse = attacks.AttackSprites(4)

        attack_list = [leaf, leaf2, crescent, tornado, tornado2, fire, pulse]
        return attack_list
    
    def build_button(x, y, image, scale):
        return_button = Button(x, y, image, scale)
        return return_button
    
    def build_inst_txt(title_font, font):
        inst_txt = []
        #Page 1     
        title_txt = title_font.render("Pokemon Catcher", True, constants.PINK)
                
        #Page 2     
        text = font.render("MOVE LEFT PRESS 'A'   MOVE RIGHT PRESS 'D'", True, constants.WHITE)
        inst_txt.append(text)

        text = font.render("THROW BALL: SPACE BAR", True, constants.WHITE)
        inst_txt.append(text)

        text = font.render("AVOID THE POKEMON ATTACKS", True, constants.WHITE)
        inst_txt.append(text)

        text = font.render("CATCH THEM ALL IF YOU CAN", True, constants.WHITE)
        inst_txt.append(text)

        return title_txt, inst_txt
        
    def build_ball(x, y):
        ball = moving_ball.PokeballSprite(x, y)
        return ball
    
    #builds txt that is not updated based on player actions
    def build_in_game_txt():
        txt_list = []

        font = pygame.font.SysFont('Agency FB', 25, True, False)
        font2 = pygame.font.SysFont('Agency FB', 35, True, False)
        bold = pygame.font.SysFont('Agency FB', 50, True, False)
        txt_list.append(font.render("Capture Count:",True,constants.BLUE))
        txt_list.append(font.render("Ball Count:", True, constants.BLUE))
        over_font = pygame.font.SysFont('Ink Free', 25, True, False)
        txt_list.append(over_font.render("Press 'Q' to quit", True, constants.RED))
        
       #pause group
        txt_list.append(font2.render("Press 'P' to Pause", True, constants.FUSCHIA))
        txt_list.append(font2.render("Press 'R' to Resume", True, constants.FUSCHIA))
        txt_list.append(bold.render("PAUSED", True, constants.FUSCHIA))

        return txt_list
    

#-------Button Class---------
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        
    def draw(self, screen):
        action = False
        #get mouse pose
        pos = pygame.mouse.get_pos()
        
        #check mouse over and clicked conds
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw the shit
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action
        
        
        
    
    def set_img(self, img, scale):
        width = img.get_width()
        height = img.get_height()
        self.image = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
        
    
  