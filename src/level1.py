import pygame
import random
import os
import constants

#--Spirte_Libraries--
import trainer_library
import moving_ball
import attacks
import enemy
import loader
#--------------------

#-- Setup Pygame and window --
pygame.init()

screen = pygame.display.set_mode(constants.size)
pygame.display.set_caption("Catcher")

run = True

#game clock
clock = pygame.time.Clock()
#------------------------------

# --- LOAD IMAGES & SPRITES ---
images = loader.construction.load_img()
sounds = loader.construction.load_SFX()

# -- build the walls --
wall_group = loader.construction.build_walls()

# -- create and fill sprite lists -- 
enemy_group, enemy_list = loader.construction.build_enemy_list()

# -- build the trainer sprite and its 'list' --
trainer, trainer_group = loader.construction.build_player(wall_group)

# -- ball sprite and its 'list' --
#ball = moving_ball.PokeballSprite()
ball_group = pygame.sprite.Group()

# -- attack sprites --
attack_list = loader.construction.build_attack_list()
attack_group = pygame.sprite.Group()

# -- In Game Display TxT
txt_list = loader.construction.build_in_game_txt()
#----------------------------
# --- GAME VARIABLES ---
capture_count = 0
death = 0
ball_count = 12
paused = False
disp_inst = True
death_num = 0
game_over = False
instruct_pg = 0
#-----------------------

# -------------- FUNCTIONS ------------------
def pause():
    paused = True

    temp_list = enemy_group.sprites()
    list(map(lambda x:x.stop(), temp_list))

    temp_list2 = attack_group.sprites()
    list(map(lambda x:x.stop(), temp_list2))

    ball.stop()
    trainer.stop()

def resume():
    paused = False
    temp_list = enemy_group.sprites()
    list(map(lambda x:x.go(), temp_list))

    temp_list2 = attack_group.sprites()
    list(map(lambda x:x.go_down(), temp_list2))

    ball.go_up()
    
#-------------------------------------------------

#---------- INSTRUCTION PAGES --------------------
next_button = loader.Button(825, 580, images[0], 0.5)
font = pygame.font.Font(None, 36)
title_font = pygame.font.SysFont('BankGothic Md BT', 60, True, constants.PINK)
title_txt, inst_txt = loader.construction.build_inst_txt(title_font, font)

while run: 
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    while instruct_pg != 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        screen.blit(images[2], [0,0])
        if next_button.draw(screen) == True:
            instruct_pg += 1
            sounds[2].play()

        # Draw instructions, page 1
        if instruct_pg == 0:
            screen.blit(title_txt, [325, 300])
        
        # Draw instructions, page 2
        if instruct_pg == 1:
            next_button.set_img(images[1], 0.5)
        
            i = 0
            y = 100
            for x in inst_txt:
                screen.blit(inst_txt[i], [200, y])
                y += 30
                i += 1
        

        clock.tick(60)

        pygame.display.flip()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #--- Key Commands ---
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and paused == False:
                    trainer.go_left()
                if event.key == pygame.K_d and paused == False:
                    trainer.go_right()
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_p:
                    pause()
                    
                if event.key == pygame.K_r:
                    resume()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and trainer.change_x < 0:
                    trainer.stop()
                if event.key == pygame.K_d and trainer.change_x > 0:
                    trainer.stop()
                if event.key == pygame.K_SPACE and paused == False and ball_count != 0:
                    ball = loader.construction.build_ball(trainer.rect.x, trainer.rect.y)
                    ball_group.add(ball)
                    ball.go_up()
                    sounds[0].play()
                    ball_count -= 1
        
        if (ball_count == 0 and not ball_group.sprites()) or death >= 1 or capture_count == 7:
            game_over = True 
                    
        i = 0
        
        for attack in attack_list:
            if attack_list[i] == random.randrange(0, 500):
                attack_list[i].rect.x = enemy_list[i].rect.x    
                attack_list[i].rect.y = enemy_list[i].rect.y
                attack_list[i].go_down()
                attack_group.add(attack_list[i])
                i += 1

        #----- UPDATE ALL THE SHIT -----
        trainer_group.update()
        ball_group.update()
        attack_group.update()
        enemy_group.update()
        #-------------------------------

        #----- CHECK FOR ANY COLLISIONS -----
        for attack in attack_group:
            hit_list = pygame.sprite.spritecollide(trainer, attack_group)
            col_list = pygame.sprite.spritecollide(trainer, enemy_group)
        
            if hit_list or col_list:
                death = 1
                trainer_group.clear()
                ball_group.clear()

        for ball in ball_group:
            caught_list = pygame.sprite.spritecollide(ball, enemy_group, True)

            for item in caught_list: 
                ball_group.remove(ball)
                enemy_group.remove(item)
                attack_group.remove(item.atck_num)
                capture_count += 1
                ball_count -= 1
                item.caught - True
                sounds[1].play()

        #check for collsions with the player and walls
        for wall in wall_group:
            wall_hit_list = pygame.sprite.spritecollide(wall, ball_group, True)
            
            for item in wall_hit_list:
                ball_count -= 1

        #bounce the enemies off the walls
        for guy in enemy_group:
            if guy.rect.x < 0 or guy.rect.x > 950:
                guy.change_x *= -1
            if guy.rect.y < 0 or guy.rect.y > 550:
                guy.change_y *= -1

        #generate text for HUD
        number = font.render(str(capture_count),True,constants.BLUE)
        ball_number = font.render(str(ball_count), True, constants.BLUE)

        #----------------------- Time to Draw Shit -----------------------------------

        #- Start with the background -
        screen.fill(constants.PINK)
        screen.blit(images[2], [0,0])

        #- Sprites Next - 
        enemy_group.draw(screen)
        attack_group.draw(screen)
        trainer_group.draw(screen)
        ball_group.draw(screen)
        wall_group.draw(screen)

        #-Shapes-
        pygame.draw.rect(screen, constants.WHITE, [0, 594, 600, 400])
        pygame.draw.rect(screen, constants.BLACK, [600, 594, 1200, 900])

        #-- Images & txt --
        screen.blit(txt_list[0], [0,600])
        screen.blit(number, [150, 600])
        screen.blit(txt_list[1], [0, 670])
        screen.blit(ball_number, [110, 670])

        screen.blit(txt_list[2], [620, 600])
        screen.blit(txt_list[3], [620, 670])

        if paused == True:
            screen.blit(txt_list[4], [620, 670])
            screen.blit(txt_list[5], [400, 250])

        for x in range(7):
            screen.blit(images[x+8], [200+(50*x), 620])

                # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
