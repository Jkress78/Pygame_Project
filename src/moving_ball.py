#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jameskress
#
# Created:     20/12/2018
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

from Sprite_sheet2 import SpriteSheet
class PokeballSprite(pygame.sprite.Sprite):
    # -- Attributes
    # Set speed vector of player

    change_y = 0

    # This holds all the images for the animated walk left/right
    # of our player

    throwing_frames = []

    # What direction is the player facing?
    direction = "U"

    # -- Methods
    def __init__(self, x, y):


        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("ball-sheet.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(115, 12, 14, 14)
        self.throwing_frames.append(image)
        image = sprite_sheet.get_image(3, 12, 14, 14)
        self.throwing_frames.append(image)
        image = sprite_sheet.get_image(19, 12, 14, 14)
        self.throwing_frames.append(image)
        image = sprite_sheet.get_image(35, 12, 14, 14)
        self.throwing_frames.append(image)
        image = sprite_sheet.get_image(51, 12, 14, 14)
        self.throwing_frames.append(image)
        image = sprite_sheet.get_image(67, 12, 14, 14)
        self.throwing_frames.append(image)
        image = sprite_sheet.get_image(83, 12, 14, 14)
        self.throwing_frames.append(image)
        image = sprite_sheet.get_image(99, 12, 14, 14)
        self.throwing_frames.append(image)


        # Set the image the player starts with
        self.image = self.throwing_frames[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
    def update(self):

        # Move up
        self.rect.y += self.change_y
        pos = self.rect.y
        if self.direction == "U":
            frame = (pos // 15) % len(self.throwing_frames)
            self.image = self.throwing_frames[frame]

    def go_up(self):
        #UP
        self.change_y = -5
        self.direction = "U"

    def stop(self):
        #Release
        self.change_y = 0

    def disappear(self):
        self.change_y = 9
        self.rect.x = -100









