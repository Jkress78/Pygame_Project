#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jameskress
#
# Created:     10/10/2018
# Copyright:   (c) jameskress 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import pygame

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x