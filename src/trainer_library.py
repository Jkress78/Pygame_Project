#-------------------------------------------------------------------------------
# Name:        module1
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
import wall_library

from sprite_sheet import SpriteSheet
def load_image(name):
    image = pygame.image.load(name)
    return image

class TrainerSprite(pygame.sprite.Sprite):
    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0

    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames_l = []
    walking_frames_r = []

    # What direction is the player facing?
    direction = "R"

    walls = None
    def __init__(self):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("sprite_sheet1.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(14, 206, 34, 46)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(78, 204, 34, 54)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(142, 207, 34, 46)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(206, 204, 34, 54)
        self.walking_frames_r.append(image)

        #LEFT FACING
        image = sprite_sheet.get_image(14, 206, 34, 46)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(78, 204, 34, 54)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(142, 207, 34, 46)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(204, 204, 40, 54)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)





        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()




    def update(self):

        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x
        if self.direction == "R":
            frame = (pos // 20) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 20) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
# Player-controlled movement:
    def go_left(self):
        #Left
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        #Right
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        #Release
        self.change_x = 0

