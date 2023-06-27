def main():
    pass

if __name__ == '__main__':
    main()

import pygame
from sprite_sheet import SpriteSheet
import constants

class AttackSprites(pygame.sprite.Sprite):
    
    #attributes shared by all attacks

    #initial speed vector along y-axis
    change_y = 0
    moving_frames = []
    direction = "D"
    rate = -1
    temp = 0
    def __init__(self, num):
        #start by calling the parent constructor
        pygame.sprite.Sprite.__init__(self)

        #check for wich attack to build
        match num:
            case 0:
                self.build_leaf()
            case 1:
                self.build_cres()
            case 2:
                self.build_torn()
            case 3:
                self.build_fire()
            case 4:
                self.build_pulse()

        # Set the starting image
        self.image = self.moving_frames[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()


    def build_leaf(self):
        self.rate = 1
        self.temp = 1
        
        sprite_sheet = SpriteSheet("Leaf-sheet.png")
        # Load all of the images into a list
        image = sprite_sheet.get_image(1, 1, 28, 26, constants.BLACK)
        self.moving_frames.append(image)
        image = sprite_sheet.get_image(32, 1, 26, 26, constants.BLACK)
        self.moving_frames.append(image)
        image = sprite_sheet.get_image(2, 29, 26, 26, constants.BLACK)
        self.moving_frames.append(image)
        image = sprite_sheet.get_image(32, 29, 26, 26, constants.BLACK)
        self.moving_frames.append(image)

    def build_cres(self):
        self.rate = 2
        self.temp = 2
        sprite_sheet = SpriteSheet("crescent-sheet.png")
        # Load all of the images into a list
        image = sprite_sheet.get_image(1, 0, 23, 23, constants.BLACK)
        self.moving_frames.append(image)
        image = sprite_sheet.get_image(27, 0, 23, 23, constants.BLACK)
        self.moving_frames.append(image)
        image = sprite_sheet.get_image(1, 25, 23, 23, constants.BLACK)
        self.moving_frames.append(image)
        image = sprite_sheet.get_image(27, 25, 23, 23, constants.BLACK)
        self.moving_frames.append(image)

    def build_torn(self):
        self.rate = 3
        self.temp = 3
        sprite_sheet = SpriteSheet("woosh-sheet.png")
        # Load all of the images into a list
        image = sprite_sheet.get_image(1, 1, 21, 18, constants.BLACK)
        self.moving_frames.append(image)
        image = sprite_sheet.get_image(25, 1, 18, 21, constants.BLACK)
        self.moving_frames.append(image)
        image = sprite_sheet.get_image(1, 26, 21, 18, constants.BLACK)
        self.moving_frames.append(image)
        image = sprite_sheet.get_image(26, 24, 18, 21, constants.BLACK)
        self.moving_frames.append(image)

    def build_fire(self):
        self.rate = 4
        self.temp = 4
        sprite_sheet = SpriteSheet("fire-sheet.png")
        # Load all of the images into a list
        image = sprite_sheet.get_image(1, 1, 16, 25, constants.BLACK)
        self.moving_frames.append(image)
        image = sprite_sheet.get_image(19, 1, 16, 25, constants.BLACK)
        self.moving_frames.append(image)

    def build_pulse(self):
        self.rate = 5
        self.temp = 5
        sprite_sheet = SpriteSheet("pulse-sheet.png")
        # Load all of the images into a list
        image = sprite_sheet.get_image(1, 1, 16, 25, constants.BLACK)
        self.moving_frames.append(image)
        image = sprite_sheet.get_image(19, 1, 16, 25, constants.BLACK)
        self.moving_frames.append(image)


    def update(self):

        self.rect.y += self.change_y
        pos = self.rect.y
        if self.direction == "D":
            frame = (pos // 30) % len(self.moving_frames)
            self.image = self.moving_frames[frame]

    def go_down(self):
        #UP
        self.change_y = 3
        self.direction = "D"
        self.rate = self.temp

    def stop(self):
        #Release
        self.change_y = 0
        self.rate = -1