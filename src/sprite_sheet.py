#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jameskress
#
# Created:     17/12/2018
# Copyright:   (c) jameskress 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import pygame
import os
import constants

class SpriteSheet(object):

    # This points to our sprite sheet image
    sprite_sheet = None

    def __init__(self, file_name):

        # Load the sprite sheet.
        os.chdir('../img')
        self.sprite_sheet = pygame.image.load(file_name).convert()
        os.chdir('../src')

    def get_image(self, x, y, width, height, trans):

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Set Transparent color
        image.set_colorkey(trans)

        # Return the image
        return image