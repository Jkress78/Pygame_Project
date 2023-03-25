#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      jameskress
#
# Created:     29/11/2018
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

from sprite_sheet import SpriteSheet
class LeafSprite(pygame.sprite.Sprite):
    # -- Attributes
    # Set speed vector of player

    change_y = 0

    # This holds all the images for the animated walk left/right
    # of our player

    moving_frames = []

    # What direction is the player facing?
    direction = "D"

    # -- Methods
    def __init__(self):


        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("leaf-sheet.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(1, 1, 28, 26, constants.BLACK)
        self.moving_frames.append(image)
        image = sprite_sheet.get_image(32, 1, 26, 26)
        self.moving_frames.append(image)
        image = sprite_sheet.get_image(2, 29, 26, 26)
        self.moving_frames.append(image)
        image = sprite_sheet.get_image(32, 29, 26, 26)
        self.moving_frames.append(image)


        # Set the image the player starts with
        self.image = self.moving_frames[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
    def update(self):

        # Move up
        self.rect.y += self.change_y
        pos = self.rect.y
        if self.direction == "D":
            # (pos // 30) means 30 frames per second 
            frame = (pos // 30) % len(self.moving_frames)
            self.image = self.moving_frames[frame]

    def go_down(self):
        #UP
        self.change_y = 3
        self.direction = "D"

    def stop(self):
        #Release
        self.change_y = 0