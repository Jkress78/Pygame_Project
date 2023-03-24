#-------------------------------------------------------------------------------
# Name:        Ball Shooter
# Purpose:
#
# Author:      jameskress
#
# Created:     05/12/2018
# Copyright:   (c) jameskress 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


import pygame
import sys
import random
import os

#---SPRITE LIBRARIES---
from trainer_library import TrainerSprite
from moving_ball import PokeballSprite
from random import seed
from random import randint
import leaf_library
import pulse_library
import crescent_library
import tornado_library
import fire_library
import wall_library

import constants
import enemy
#------------------------

pygame.init()

# Set the width and height of the screen [width, height]

screen = pygame.display.set_mode(constants.size)

pygame.display.set_caption("Catch 'em all")

# Loop until the user clicks the close button.
done = True


# Used to manage how fast the screen updates
clock = pygame.time.Clock()



#-------IMAGES/SOUNDS---------
os.chdir('../img')
next_image = pygame.image.load("NextButt.gif").convert_alpha()

start_image = pygame.image.load("startButt.gif").convert_alpha()

background_image = pygame.image.load("poppy.png").convert()

ball_out_image = pygame.image.load("ball_background.png").convert()

victory_image = pygame.image.load("victory.jpg").convert()

death_image = pygame.image.load("death.gif").convert()

bCount_image = pygame.image.load("ball.gif").convert()

ball_silhouette = pygame.image.load("ballG.gif").convert()

caterpie_image = pygame.image.load("Caterpie.gif").convert()

pidgey_image = pygame.image.load("pidg.gif").convert()

rat_image = pygame.image.load("Rat.gif").convert()

ralts_image = pygame.image.load("Ralts.gif").convert()

poocheyana_image = pygame.image.load("Poocheyana.gif").convert()

dratini_image = pygame.image.load("Dratini.gif").convert()

drifloon_image = pygame.image.load("Drifloon.gif").convert()

caterpie_silhouette = pygame.image.load("Blackout_C.gif").convert()

pidgey_silhouette = pygame.image.load("Blackout_P.gif").convert()

rat_silhouette = pygame.image.load("Blackout_RT.gif").convert()

ralts_silhouette = pygame.image.load("Blackout_R.gif").convert()

poocheyana_silhouette = pygame.image.load("Blackout_PO.gif").convert()

dratini_silhouette = pygame.image.load("Blackout_DR.gif").convert()

drifloon_silhouette = pygame.image.load("Blackout_D.gif").convert()

#--Switch to the sfx dir of sounds--

os.chdir('../sfx')
throw = pygame.mixer.Sound("throw.ogg")

catch = pygame.mixer.Sound("ball - catch.ogg")

transition_sound = pygame.mixer.Sound("skip.ogg")

victory_sound = pygame.mixer.Sound("victory.ogg")

lose_sound = pygame.mixer.Sound("lose.ogg")

game_noise = pygame.mixer.Sound("game_sound.ogg")


#--change back to the original wd
os.chdir('../src')

#-----------WALLS-----------
wall_list = pygame.sprite.Group()
#Left
wall = wall_library.Wall(-10, 0, 10, 900)
wall_list.add(wall)

#Right
wall = wall_library.Wall(1000, 0, 10, 900)
wall_list.add(wall)

#Top
wall = wall_library.Wall(0, -10, 1000, 10)
wall_list.add(wall)


#--------------------------------

#-------Button Class---------
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        
    def draw(self):
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
    
    


                

#----CHARACTERS------
seed(345)
poocheyana = enemy.Enemy(randint(5, 400), randint(5, 400), 5, 5, 'Poocheyana.gif', 26, 34)

ralts = enemy.Enemy(randint(5, 400), randint(5, 400), -3, -3, 'Ralts.gif', 26, 32)

drifloon = enemy.Enemy(randint(5, 400), randint(5, 400), -4, -2, 'Drifloon.gif', 28, 42)

dratini = enemy.Enemy(randint(5, 400), randint(5, 400), 4, 4, 'Dratini.gif',  32, 42)

rat = enemy.Enemy(randint(5, 400), randint(5, 400), 5, 6, 'Rat.gif', 34, 38)

caterpie = enemy.Enemy(randint(5, 400), randint(5, 400), 2, 2,  'Caterpie.gif', 32, 42)

pidgey = enemy.Enemy(randint(5, 400), randint(5, 400), -4, -5, 'pidg.gif', 34, 35)

trainer_sprit = TrainerSprite()
trainer_sprit.rect.x = 0
trainer_sprit.rect.y = 530

ball = PokeballSprite()
#--------------------------------

#---ATTACKS-----

leaf = leaf_library.LeafSprite()

leaf2 = leaf_library.LeafSprite()

crescent = crescent_library.CrescentSprite()

tornado = tornado_library.TornadoSprite()

tornado2 = tornado_library.TornadoSprite()

fire = fire_library.FireSprite()

pulse = pulse_library.DargonPSprite()

trainer_sprit.walls = wall_list

#------------LISTS---------
attack_list = pygame.sprite.Group()

pokemon_list = pygame.sprite.Group(caterpie, rat, pidgey, ralts, poocheyana, drifloon, dratini)

player_list = pygame.sprite.Group(trainer_sprit)

ball_list = pygame.sprite.Group()

trainer_list = pygame.sprite.Group(trainer_sprit)

rat_list = pygame.sprite.Group(rat)

caterpie_list = pygame.sprite.Group(caterpie)

pidgey_list = pygame.sprite.Group(pidgey)

ralts_list = pygame.sprite.Group(ralts)

poocheyana_list = pygame.sprite.Group(poocheyana)

dratini_list = pygame.sprite.Group(dratini)

drifloon_list = pygame.sprite.Group(drifloon)
#----------------------------------------------------------------------


#--------------------------VARIABLES----------------
capture_count = 0
pokeball_count = 12
ball_count = 12
ball_type = 1

paused = False

dratini_catch = False

drifloon_catch = False

ralts_catch = False

poocheyanna_catch = False

caterpie_catch = False

pidgey_catch = False

rat_catch = False

rat_directX = 1
rat_directY = 1

cat_directX = 1
cat_directY = 1

pid_directX = 1
pid_directY = 1

dra_directX = 1
dra_directY = 1

dri_directX = 1
dri_directY = 1

poo_directX = 1
poo_directY = 1

ral_directX = 1
ral_directY = 1
#----------------------------------------------

#----------------ATTACK RATES-----
leaf_shoot = 5

tornado_shoot = 5

leaf_shoot2 = 5

tornado_shoot2 = 5

crescent_shoot = 5

fire_shoot = 5

pulse_shoot = 5
#-------------------------------


#-----------------------------------Functions------------------------------------------
def pause():
    ball.stop()
    trainer_sprit.stop()
    
    rat.stop()
    caterpie.stop()
    dratini.stop()
    drifloon.stop()
    pidgey.stop()
    poocheyana.stop()
    ralts.stop()
    
    crescent.stop()
    leaf.stop()
    leaf2.stop()
    tornado.stop()
    tornado2.stop()
    fire.stop()
    pulse.stop()
    
def resume():
    ball.go_up()
    
    rat.change_x = 5 * rat_directX
    rat.change_y = 6 * rat_directY
    
    caterpie.change_x = 2 * cat_directX
    caterpie.change_y = 2 * cat_directY
    
    dratini.change_x = 4 * dra_directX
    dratini.change_y = 4 * dra_directY
    
    drifloon.change_x = -4 * dri_directX
    drifloon.change_y = -2 * dri_directY
    
    pidgey.change_x = -4 * pid_directX
    pidgey.change_y = -5 * pid_directY
    
    poocheyana.change_x = 5 * poo_directX
    poocheyana.change_y = 5 * poo_directY
    
    ralts.change_x = -3 * ral_directX
    ralts.change_y = -3 * ral_directY
    
    crescent.go_down()
    leaf.go_down()
    leaf2.go_down()
    tornado.go_down()
    tornado2.go_down()
    fire.go_down()
    pulse.go_down()
    

   
#--------------------------------------------------------

#Intro Pages
display_instructions = True
instruction_page = 1
font = pygame.font.Font(None, 36)
next_button = Button(825, 580, next_image, 0.5)
start_button = Button(825, 580, start_image, 0.5)

#END GAME
death = 0
game_over = False
#----------------Instruction Page Loop---------
while done and instruction_page != 3:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

        if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_SPACE:
                #instruction_page += 1
                #transition_sound.play()
                if instruction_page == 3:
                    display_instructions = False
                    game_noise.play()


        

    screen.fill(constants.BLACK)
    screen.blit(background_image,[0,0])
    
    
    
    
    if next_button.draw() == True:
        instruction_page += 1 
        transition_sound.play()
    # Draw instructions, page 1
    if instruction_page == 1:
                       
        
        title_font = pygame.font.SysFont('BankGothic Md BT', 60, True, constants.PINK)

        text = title_font.render("Pokemon Catcher", True, constants.PINK)
        screen.blit(text, [325, 300])

        
        
    if instruction_page == 2:
               
        # Draw instructions, page 2
        text = font.render("MOVE LEFT PRESS 'A'   MOVE RIGHT PRESS 'D'", True, constants.WHITE)
        screen.blit(text, [200, 100])

        text = font.render("THROW BALL: SPACE BAR", True, constants.WHITE)
        screen.blit(text, [200, 130])

        text = font.render("AVOID THE POKEMON ATTACKS", True, constants.WHITE)
        screen.blit(text, [200, 160])

        text = font.render("CATCH THEM ALL IF YOU CAN", True, constants.WHITE)
        screen.blit(text, [200, 190])

        


    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()



# -------- Main Program Loop -----------
while done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False


        #--------pressed down on key-------

        
        
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and paused == False:
                    trainer_sprit.go_left()
                if event.key == pygame.K_d and paused == False:
                    trainer_sprit.go_right()
                if event.key == pygame.K_q:
                    done = False
                


 #----------let up on a key---------
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a and trainer_sprit.change_x < 0:
                    trainer_sprit.stop()
                    
            if event.key == pygame.K_d and trainer_sprit.change_x > 0:
                    trainer_sprit.stop()
                    
            if event.key == pygame.K_p:
                pause()
                paused = True
                crescent_shoot = -9
                leaf_shoot2 = -9
                leaf_shoot = -9
                fire_shoot = -9
                pulse_shoot = -9
                tornado_shoot = -9
                tornado_shoot2 = -9
                
            if event.key == pygame.K_r and paused == True:
                resume()
                paused = False
                if rat_catch == False:
                    crescent_shoot = 5
                if ralts_catch == False:
                    leaf_shoot2 = 5
                if caterpie_catch == False:
                    leaf_shoot = 5
                if poocheyanna_catch == False:
                    fire_shoot = 5
                if dratini_catch == False:
                    pulse_shoot = 5
                if pidgey_catch == False:
                    tornado_shoot = 5
                if drifloon_catch == False:
                    tornado_shoot2 = 5                
            
                

        if pokeball_count != 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and paused == False:
                    ball = PokeballSprite()
                    ball.rect.x = trainer_sprit.rect.x
                    ball.rect.y = trainer_sprit.rect.y
                    ball_list.add(ball)
                    ball.go_up()
                    throw.play()
                    pokeball_count -= 1








#---------Not Dead Loop------------------------------
    if not game_over:

        if ball_count == 0 or death >= 1 or capture_count == 7:
            game_over = True



    # -----------------ATTACK RATES--------------------------
        if tornado_shoot == random.randrange(0, 500):
            tornado = tornado_library.TornadoSprite()
            tornado.rect.x = pidgey.rect.x
            tornado.rect.y = pidgey.rect.y
            tornado.go_down()
            attack_list.add(tornado)

        if leaf_shoot == random.randrange(0, 500):
           leaf = leaf_library.LeafSprite()
           leaf.rect.x = caterpie.rect.x
           leaf.rect.y = caterpie.rect.y
           leaf.go_down()
           attack_list.add(leaf)

        if crescent_shoot == random.randrange(0, 520):
          crescent = crescent_library.CrescentSprite()
          crescent.rect.x = rat.rect.x
          crescent.rect.y = rat.rect.y
          crescent.go_down()
          attack_list.add(crescent)

        if tornado_shoot2 == random.randrange(0, 520):
            tornado2 = tornado_library.TornadoSprite()
            tornado2.rect.x = drifloon.rect.x
            tornado2.rect.y = drifloon.rect.y
            tornado2.go_down()
            attack_list.add(tornado2)

        if leaf_shoot2 == random.randrange(0, 520):
           leaf2 = leaf_library.LeafSprite()
           leaf2.rect.x = ralts.rect.x
           leaf2.rect.y = ralts.rect.y
           leaf2.go_down()
           attack_list.add(leaf2)

        if fire_shoot == random.randrange(0, 520):
            fire = fire_library.FireSprite()
            fire.rect.x = poocheyana.rect.x
            fire.rect.y = poocheyana.rect.y
            fire.go_down()
            attack_list.add(fire)

        if pulse_shoot == random.randrange(0, 520):
            pulse = pulse_library.DargonPSprite()
            pulse.rect.x = dratini.rect.x
            pulse.rect.y = dratini.rect.y
            pulse.go_down()
            attack_list.add(pulse)
    #------------------------------------------------------














            #---update-----
        trainer_list.update()
        ball_list.update()
        attack_list.update()
        rat_list.update()
        caterpie_list.update()
        pidgey_list.update()
        poocheyana_list.update()
        ralts_list.update()
        drifloon_list.update()
        dratini_list.update()
        #---------------------------

      #-----------Attack Collisions---------------
        for attack in attack_list:

                hit_list = pygame.sprite.spritecollide(crescent, trainer_list, True)
                collision_list = pygame.sprite.spritecollide(rat, trainer_list, True)

                hit_list2 = pygame.sprite.spritecollide(leaf, trainer_list, True)
                collision_list2 = pygame.sprite.spritecollide(caterpie, trainer_list, True)

                hit_list3 = pygame.sprite.spritecollide(tornado, trainer_list, True)
                collision_list3 = pygame.sprite.spritecollide(pidgey, trainer_list, True)

                hit_list4 = pygame.sprite.spritecollide(pulse, trainer_list, True)
                collision_list4 = pygame.sprite.spritecollide(dratini, trainer_list, True)

                hit_list5 = pygame.sprite.spritecollide(leaf2, trainer_list, True)
                collision_list5 = pygame.sprite.spritecollide(ralts, trainer_list, True)

                hit_list6 = pygame.sprite.spritecollide(tornado2, trainer_list, True)
                collision_list6 = pygame.sprite.spritecollide(drifloon, trainer_list, True)

                hit_list7 = pygame.sprite.spritecollide(fire, trainer_list, True)
                collision_list7 = pygame.sprite.spritecollide(poocheyana, trainer_list, True)



                for trainer in hit_list:
                    death = 1
                    trainer_list.remove(trainer_sprit)
                    ball_list.remove(ball)
                for trainer in collision_list:
                    death = 1
                    trainer_list.remove(trainer_sprit)
                    ball_list.remove(ball)

                for trainer in hit_list2:
                    death = 2
                    trainer_list.remove(trainer_sprit)
                    ball_list.remove(ball)
                for trainer in collision_list2:
                    death = 2
                    trainer_list.remove(trainer_sprit)
                    ball_list.remove(ball)

                for trainer in hit_list3:
                    death = 3
                    trainer_list.remove(trainer_sprit)
                    ball_list.remove(ball)
                for trainer in collision_list3:
                    death = 3
                    trainer_list.remove(trainer_sprit)
                    ball_list.remove(ball)

                for trainer in hit_list4:
                    death = 4
                    trainer_list.remove(trainer_sprit)
                    ball_list.remove(ball)
                for trainer in collision_list4:
                    death = 4
                    trainer_list.remove(trainer_sprit)
                    ball_list.remove(ball)

                for trainer in hit_list5:
                    death = 5
                    trainer_list.remove(trainer_sprit)
                    ball_list.remove(ball)
                for trainer in collision_list5:
                    death = 5
                    trainer_list.remove(trainer_sprit)
                    ball_list.remove(ball)

                for trainer in hit_list6:
                    death = 6
                    trainer_list.remove(trainer_sprit)
                    ball_list.remove(ball)
                for trainer in collision_list6:
                    death = 6
                    trainer_list.remove(trainer_sprit)
                    ball_list.remove(ball)

                for trainer in hit_list7:
                    death = 7
                    trainer_list.remove(trainer_sprit)
                    ball_list.remove(ball)
                for trainer in collision_list7:
                    death = 7
                    trainer_list.remove(trainer_sprit)
                    ball_list.remove(ball)





                # Calculate mechanics for each ball
        for ball in ball_list:
                #check for a capture
                rat_capture_list = pygame.sprite.spritecollide(ball, rat_list, True)

                pidgey_capture_list = pygame.sprite.spritecollide(ball, pidgey_list, True)

                caterpie_capture_list = pygame.sprite.spritecollide(ball, caterpie_list, True)

                ralts_capture_list = pygame.sprite.spritecollide(ball, ralts_list, True)

                dratini_capture_list = pygame.sprite.spritecollide(ball, dratini_list, True)

                drifloon_capture_list = pygame.sprite.spritecollide(ball, drifloon_list, True)

                poocheyana_capture_list = pygame.sprite.spritecollide(ball, poocheyana_list, True)





                # For each pokemon catch remove pokemons attack
                for item in rat_capture_list:
                    ball_list.remove(ball)
                    attack_list.remove(crescent)
                    pokemon_list.remove(rat)
                    rat_list.remove(rat)
                    rat_catch = True
                    capture_count += 1
                    crescent_shoot = -9
                    ball_count -= 1
                    catch.play()

                for item in pidgey_capture_list:
                    ball_list.remove(ball)
                    attack_list.remove(tornado)
                    pidgey_list.remove(pidgey)
                    pokemon_list.remove(pidgey)
                    pidgey_catch = True
                    capture_count += 1
                    tornado_shoot = -9
                    ball_count -= 1
                    catch.play()

                for item in caterpie_capture_list:
                    ball_list.remove(ball)
                    attack_list.remove(leaf)
                    pokemon_list.remove(caterpie)
                    caterpie_list.remove(caterpie)
                    caterpie_catch = True
                    capture_count += 1
                    leaf_shoot = -9
                    ball_count -= 1
                    catch.play()

                for item in ralts_capture_list:
                    ball_list.remove(ball)
                    attack_list.remove(leaf2)
                    pokemon_list.remove(ralts)
                    ralts_list.remove(ralts)
                    ralts_catch = True
                    capture_count += 1
                    leaf_shoot2 = -9
                    ball_count -= 1
                    catch.play()

                for item in poocheyana_capture_list:
                    ball_list.remove(ball)
                    attack_list.remove(fire)
                    pokemon_list.remove(poocheyana)
                    poocheyana_list.remove(poocheyana)
                    poocheyanna_catch = True
                    capture_count += 1
                    fire_shoot = -9
                    ball_count -= 1
                    catch.play()

                for item in drifloon_capture_list:
                    ball_list.remove(ball)
                    attack_list.remove(tornado2)
                    pokemon_list.remove(drifloon)
                    drifloon_list.remove(drifloon)
                    drifloon_catch = True
                    capture_count += 1
                    tornado_shoot2 = -9
                    ball_count -= 1
                    catch.play()

                for item in dratini_capture_list:
                    ball_list.remove(ball)
                    attack_list.remove(pulse)
                    pokemon_list.remove(dratini)
                    dratini_list.remove(dratini)
                    dratini_catch = True
                    capture_count += 1
                    pulse_shoot = -9
                    ball_count -= 1
                    catch.play()


        for wall in wall_list:

            wall_hit_list = pygame.sprite.spritecollide(wall, ball_list, True)

            for item in wall_hit_list:

                    ball_count -= 1











#---------------Bounce------------------
        if rat.rect.x > 950 or rat.rect.x < 0:
            rat.change_x = rat.change_x * -1
            rat_directX *= -1
        if rat.rect.y > 550 or rat.rect.y <0:
            rat.change_y = rat.change_y *-1
            rat_directY *= -1
            

        if caterpie.rect.x > 950 or caterpie.rect.x <0:
            caterpie.change_x = caterpie.change_x *-1
            cat_directX *= -1
        if caterpie.rect.y > 550 or caterpie.rect.y <0:
            caterpie.change_y = caterpie.change_y *-1
            cat_directY *= -1

        if pidgey.rect.x < 0 or pidgey.rect.x > 950:
            pidgey.change_x = pidgey.change_x *-1
            pid_directX *= -1 
        if pidgey.rect.y > 550 or pidgey.rect.y <0:
            pidgey.change_y = pidgey.change_y *-1
            pid_directY *= -1

        if ralts.rect.x < 0 or ralts.rect.x > 950:
            ralts.change_x = ralts.change_x *-1
            ral_directX *= -1
        if ralts.rect.y > 550 or ralts.rect.y <0:
            ralts.change_y = ralts.change_y *-1
            ral_directY *= -1

        if dratini.rect.x < 0 or dratini.rect.x > 950:
            dratini.change_x = dratini.change_x *-1
            dra_directX *= -1
        if dratini.rect.y > 550 or dratini.rect.y <0:
            dratini.change_y = dratini.change_y *-1
            dra_directY *= -1

        if poocheyana.rect.x < 0 or poocheyana.rect.x > 950:
            poocheyana.change_x = poocheyana.change_x * -1
            poo_directX *= -1
        if poocheyana.rect.y > 550 or poocheyana.rect.y < 0:
            poocheyana.change_y = poocheyana.change_y * -1
            poo_directY *= -1

        if drifloon.rect.x < 0 or drifloon.rect.x > 950:
            drifloon.change_x = drifloon.change_x * -1
            dri_directX *= -1
        if drifloon.rect.y > 550 or drifloon.rect.y < 0:
            drifloon.change_y = drifloon.change_y * -1
            dri_directY *= -1
        



#--------------------------Text----------------------------------
        font = pygame.font.SysFont('Agency FB', 25, True, False)
        
        font2 = pygame.font.SysFont('Agency FB', 35, True, False)
        
        bold = pygame.font.SysFont('Agency FB', 50, True, False)

        text = font.render("Capture Count:",True,constants.BLUE)

        number = font.render(str(capture_count),True,constants.BLUE)

        ball_text = font.render("Ball Count:", True, constants.BLUE)

        ball_number = font.render(str(pokeball_count), True, constants.BLUE)

        ball_type_number = font.render(str(ball_type), True, constants.BLUE)
        
        over_font = pygame.font.SysFont('Ink Free', 25, True, False)
        over_text = over_font.render("Press 'Q' to quit", True, constants.RED)
        
        if paused == False:
            pause_text = font2.render("Press 'P' to Pause", True, constants.FUSCHIA)
        if paused == True: 
            pause_text = font2.render("Press 'R' to Resume", True, constants.FUSCHIA)
        pauseT = bold.render("PAUSED", True, constants.FUSCHIA)
#-------------------------------------------------------------------
          

            #-----draw background----------
        screen.fill(constants.PINK)
        screen.blit(background_image,[0,0])


            #------drawing sprites------

        pokemon_list.draw(screen)
        attack_list.draw(screen)
        trainer_list.draw(screen)
        ball_list.draw(screen)
        wall_list.draw(screen)
        pygame.draw.rect(screen, constants.WHITE, [0, 594, 600, 400])
        pygame.draw.rect(screen, constants.BLACK, [600, 594, 1200, 900])

        
        #-----------Images & Texts---------------
        screen.blit(text, [0, 600])
        screen.blit(number, [150, 600])
        screen.blit(ball_text, [0, 670])
        screen.blit(ball_number, [110, 670])
        
        screen.blit(pause_text, [620, 600])
        screen.blit(over_text, [620, 670])
        
        if paused == True:
            screen.blit(pauseT, [400, 250])

        #----------------Silhouettes---------------------
        screen.blit(caterpie_silhouette, [200, 620])

        screen.blit(rat_silhouette, [250, 620])

        screen.blit(pidgey_silhouette, [300, 620])

        screen.blit(ralts_silhouette, [350, 620])

        screen.blit(poocheyana_silhouette, [400, 620])

        screen.blit(drifloon_silhouette, [450, 620])

        screen.blit(dratini_silhouette, [500, 620])
    #------------------------------------------------

        if caterpie_catch == True:
            screen.blit(caterpie_image, [200, 620])

        if rat_catch == True:
            screen.blit(rat_image, [250, 620])

        if pidgey_catch == True:
            screen.blit(pidgey_image, [300, 620])

        if ralts_catch == True:
            screen.blit(ralts_image, [350, 620])

        if poocheyanna_catch == True:
            screen.blit(poocheyana_image, [400, 620])

        if drifloon_catch == True:
            screen.blit(drifloon_image, [450, 620])

        if dratini_catch == True:
            screen.blit(dratini_image, [500, 620])
#----------------------------------------------------

        screen.blit(bCount_image, [150, 670])
        screen.blit(bCount_image, [170, 670])
        screen.blit(bCount_image, [190, 670])
        screen.blit(bCount_image, [210, 670])
        screen.blit(bCount_image, [230, 670])
        screen.blit(bCount_image, [250, 670])
        screen.blit(bCount_image, [270, 670])
        screen.blit(bCount_image, [290, 670])
        screen.blit(bCount_image, [310, 670])
        screen.blit(bCount_image, [330, 670])
        screen.blit(bCount_image, [350, 670])
        screen.blit(bCount_image, [370, 670])
        
        if pokeball_count <= 11:
            screen.blit(ball_silhouette, [150, 670])
        if pokeball_count <= 10:
            screen.blit(ball_silhouette, [170, 670])
        if pokeball_count <= 9:
            screen.blit(ball_silhouette, [190, 670])
        if pokeball_count <= 8:
            screen.blit(ball_silhouette, [210, 670])       
        if pokeball_count <= 7:
            screen.blit(ball_silhouette, [230, 670])
        if pokeball_count <= 6:
            screen.blit(ball_silhouette, [250, 670])
        if pokeball_count <= 5:
            screen.blit(ball_silhouette, [270, 670])
        if pokeball_count <= 4:
            screen.blit(ball_silhouette, [290, 670])
        if pokeball_count <= 3:
            screen.blit(ball_silhouette, [310, 670])
        if pokeball_count <= 2:
            screen.blit(ball_silhouette, [330, 670])
        if pokeball_count <= 1:
            screen.blit(ball_silhouette, [350, 670])
        if pokeball_count <= 0:
            screen.blit(ball_silhouette, [370, 670])
            
            







#---------------------GAME OVER----------------------
    if game_over:
        game_noise.stop()

    #-----------------RESET-------------------------
        if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:

                        victory_sound.stop()
                        lose_sound.stop()
                        game_noise.play()
                        done = False
                        doone = True
                        game_over = False
                        display_instructions = True
                        instruction_page = 1
                        death = 0
                        capture_count = 0
                        ball_count = 12
                        pokeball_count = 12

                        size = (1000, 700)
                        screen = pygame.display.set_mode(size)




                        trainer_sprit.rect.x = 5
                        ball.rect.x = -100
                        dratini.rect.y = 50
                        ralts.rect.y = 100
                        drifloon.rect.y = 25
                        poocheyana.rect.y = 75
                        pidgey.rect.y = 125
                        caterpie.rect.y = 20
                        rat.rect.y = 10

                        leaf.rect.x = -100
                        leaf2.rect.x = -111
                        fire.rect.x = -111
                        crescent.rect.x = -123
                        pulse.rect.x = -456
                        tornado.rect.x = -789
                        tornado2.rect.x = -101112

                        trainer_list.add(trainer_sprit)


                        if dratini_catch == 1:
                            dratini_catch = 0
                            pokemon_list.add(dratini)
                            dratini_list.add(dratini)
                            attack_list.add(pulse)
                            pulse_shoot = random.randrange(0, 500)

                        if drifloon_catch ==1:
                            drifloon_catch = 0
                            drifloon_list.add(drifloon)
                            pokemon_list.add(drifloon)
                            attack_list.add(tornado2)
                            tornado_shoot2 = random.randrange(0, 500)

                        if ralts_catch == 1:
                            ralts_catch = 0
                            ralts_list.add(ralts)
                            pokemon_list.add(ralts)
                            attack_list.add(leaf2)
                            leaf_shoot2 = random.randrange(0, 500)

                        if poocheyanna_catch == 1:
                            poocheyanna_catch = 0
                            poocheyana_list.add(poocheyana)
                            pokemon_list.add(poocheyana)
                            attack_list.add(fire)
                            fire_shoot = random.randrange(0, 500)

                        if caterpie_catch == 1:
                            caterpie_catch = 0
                            caterpie_list.add(caterpie)
                            pokemon_list.add(caterpie)
                            attack_list.add(leaf)
                            leaf_shoot = random.randrange(0, 500)

                        if pidgey_catch == 1:
                            pidgey_catch = 0
                            pidgey_list.add(pidgey)
                            pokemon_list.add(pidgey)
                            attack_list.add(tornado)
                            tornado_shoot = random.randrange(0, 500)

                        if rat_catch == 1:
                            rat_catch = 0
                            rat_list.add(rat)
                            pokemon_list.add(rat)
                            attack_list.add(crescent)
                            crescent_shoot = random.randrange(0, 500)

                        for ball in ball_list:
                            ball.disappear()
    #-------------------------------------------------------------------


        font = pygame.font.SysFont('Ink Free', 30, True, False)
        quit_font = pygame.font.SysFont('Ink Free', 25, True, False)



        if ball_count <= 0 and capture_count != 7:
            lose_sound.play()
            size = (600, 500)
            screen  = pygame.display.set_mode(size)



            screen.blit(ball_out_image, [-200, -200])
            text = font.render("YOU RAN OUT OF BALLS", True, constants.BLUE)
            text2 = font.render("You Caught", True, constants.BLUE)
            text3 = font.render(str(capture_count), True, constants.BLUE)
            text4 = font.render("Pokemon", True, constants.BLUE)
            restart = quit_font.render("Press R to restart", True, constants.FUSCHIA)
            quit_text = quit_font.render("Press Q to quit", True, constants.RED)
            screen.blit(text, [100,100])
            screen.blit(text2, [100, 150])
            screen.blit(text3, [290, 150])
            screen.blit(text4, [320, 150])
            screen.blit(restart, [10, 470])
            screen.blit(quit_text, [400, 470])
            if rat_catch == 1:
                screen.blit(rat_image, [100, 200])
            if caterpie_catch == 1:
                screen.blit(caterpie_image, [150, 200])
            if pidgey_catch == 1:
                screen.blit(pidgey_image, [200, 200])
            if ralts_catch == 1:
                screen.blit(ralts_image, [250, 200])
            if poocheyanna_catch == 1:
                screen.blit(poocheyana_image, [300, 200])
            if drifloon_catch == 1:
                screen.blit(drifloon_image, [350, 200])
            if dratini_catch == 1:
                screen.blit(dratini_image, [400, 200])




        elif capture_count == 7:
            size = (626, 626)
            screen  = pygame.display.set_mode(size)
            screen.blit(victory_image, [0,0])
            victory_sound.play()



            font = pygame.font.SysFont('Agency FB', 50, True, constants.PINK)
            text = font.render("YOU CAUGHT THEM ALL", True, constants.PINK)
            font = pygame.font.SysFont('Agency FB', 25, True, constants.PINK)
            text2 = quit_font.render("Press Q to quit", True, constants.RED)
            restart = quit_font.render("Press R to restart", True, constants.FUSCHIA)

            screen.blit(text, [100, 150])
            screen.blit(drifloon_image, [200, 250])
            screen.blit(rat_image, [250, 250])
            screen.blit(caterpie_image, [300, 250])
            screen.blit(pidgey_image, [350, 250])
            screen.blit(poocheyana_image, [275, 300])
            screen.blit(ralts_image, [325, 300])
            screen.blit(dratini_image, [225, 300])
            screen.blit(restart, [10, 590])
            screen.blit(text2, [400, 590])

        if death == 1:
            size = (500, 249)
            screen  = pygame.display.set_mode(size)
            screen.fill(constants.BLACK)
            lose_sound.play()

            screen.blit(death_image, [0,0])
            text  = font.render("You were Killed by Rattata", True, constants.LIME)
            text2 = quit_font.render("Press Q to quit", True, constants.RED)
            restart = quit_font.render("Press R to restart", True, constants.FUSCHIA)
            screen.blit(text, [10, 10])
            screen.blit(text2, [300, 220])
            screen.blit(rat_image, [50, 50])
            screen.blit(restart, [10, 220])

        if death == 2:
            size = (500, 249)
            screen  = pygame.display.set_mode(size)

            screen.fill(constants.BLACK)
            lose_sound.play()
            screen.blit(death_image, [0,0])
            text  = font.render("You were Killed by Caterpie", True, constants.LIME)
            text2 = quit_font.render("Press Q to quit", True, constants.RED)
            restart = quit_font.render("Press R to restart", True, constants.FUSCHIA)
            screen.blit(text, [10, 10])
            screen.blit(text2, [300, 220])
            screen.blit(caterpie_image, [50, 50])
            screen.blit(restart, [10, 220])

        if death == 3:
            size = (500, 249)
            screen  = pygame.display.set_mode(size)


            screen.fill(constants.BLACK)
            lose_sound.play()
            screen.blit(death_image, [0,0])
            text  = font.render("You were Killed by Pidgey", True, constants.LIME)
            text2 = quit_font.render("Press Q to quit", True, constants.RED)
            restart = quit_font.render("Press R to restart", True, constants.FUSCHIA)
            screen.blit(text, [10, 10])
            screen.blit(text2, [300, 220])
            screen.blit(pidgey_image, [50, 50])
            screen.blit(restart, [10, 220])

        if death == 4:
            size = (500, 249)
            screen  = pygame.display.set_mode(size)


            screen.blit(death_image, [0,0])
            lose_sound.play()
            text  = font.render("You were Killed by Dratini", True, constants.LIME)
            text2 = quit_font.render("Press Q to quit", True, constants.RED)
            restart = quit_font.render("Press R to restart", True, constants.FUSCHIA)
            screen.blit(text, [10, 10])
            screen.blit(text2, [300, 220])
            screen.blit(dratini_image, [50, 50])
            screen.blit(restart, [10, 220])

        if death == 5:
            size = (500, 249)
            screen  = pygame.display.set_mode(size)
            lose_sound.play()



            screen.fill(constants.BLACK)
            screen.blit(death_image, [0,0])
            text  = font.render("You were Killed by Ralts", True, constants.LIME)
            text2 = quit_font.render("Press Q to quit", True, constants.RED)
            restart = quit_font.render("Press R to restart", True, constants.FUSCHIA)
            screen.blit(text, [10, 10])
            screen.blit(text2, [300, 220])
            screen.blit(ralts_image, [50, 50])
            screen.blit(restart, [10, 220])

        if death == 6:
            size = (500, 249)
            screen  = pygame.display.set_mode(size)
            lose_sound.play()



            screen.fill(constants.BLACK)
            screen.blit(death_image, [0,0])
            text  = font.render("You were Killed by Drifloon", True, constants.LIME)
            text2 = quit_font.render("Press Q to quit", True, constants.RED)
            restart = quit_font.render("Press R to restart", True, constants.FUSCHIA)
            screen.blit(text, [10, 10])
            screen.blit(text2, [300, 220])
            screen.blit(drifloon_image, [50, 50])
            screen.blit(restart, [10, 220])

        if death == 7:
            size = (500, 249)
            screen  = pygame.display.set_mode(size)
            lose_sound.play()


            screen.fill(constants.BLACK)
            screen.blit(death_image, [0,0])
            text  = font.render("You were Killed by Poocheyana", True, constants.LIME)
            text2 = quit_font.render("Press Q to quit", True, constants.RED)
            restart = quit_font.render("Press R to restart", True, constants.FUSCHIA)
            screen.blit(text, [10, 10])
            screen.blit(text2, [300, 220])
            screen.blit(poocheyana_image, [50, 50])
            screen.blit(restart, [10, 220])



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
