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

    def __init__(self, name):
        #start by calling the parent constructor
        pygame.sprite.Sprite.__init__(self)

        

        #check for name match
        if name == "leaf-sheet.png":
            sprite_sheet = SpriteSheet(name)
            # Load all of the images into a list
            image = sprite_sheet.get_image(1, 1, 28, 26, constants.BLACK)
            self.moving_frames.append(image)
            image = sprite_sheet.get_image(32, 1, 26, 26, constants.BLACK)
            self.moving_frames.append(image)
            image = sprite_sheet.get_image(2, 29, 26, 26, constants.BLACK)
            self.moving_frames.append(image)
            image = sprite_sheet.get_image(32, 29, 26, 26, constants.BLACK)
            self.moving_frames.append(image)

        elif name == "crescent-sheet.png":
            sprite_sheet = SpriteSheet(name)
            # Load all of the images into a list
            image = sprite_sheet.get_image(1, 0, 23, 23, constants.BLACK)
            self.moving_frames.append(image)
            image = sprite_sheet.get_image(27, 0, 23, 23, constants.BLACK)
            self.moving_frames.append(image)
            image = sprite_sheet.get_image(1, 25, 23, 23, constants.BLACK)
            self.moving_frames.append(image)
            image = sprite_sheet.get_image(27, 25, 23, 23, constants.BLACK)
            self.moving_frames.append(image)

        elif name == "fire-sheet.png":
            sprite_sheet = SpriteSheet(name)
            # Load all of the images into a list
            image = sprite_sheet.get_image(1, 1, 16, 25, constants.BLACK)
            self.moving_frames.append(image)
            image = sprite_sheet.get_image(19, 1, 16, 25, constants.BLACK)
            self.moving_frames.append(image)

        elif name == "pulse-sheet.png":
            sprite_sheet = SpriteSheet(name)
            # Load all of the images into a list
            image = sprite_sheet.get_image(1, 1, 16, 25, constants.BLACK)
            self.moving_frames.append(image)
            image = sprite_sheet.get_image(19, 1, 16, 25, constants.BLACK)
            self.moving_frames.append(image)

        elif name == "woosh-sheet.png":
            sprite_sheet = SpriteSheet(name)
            # Load all of the images into a list
            image = sprite_sheet.get_image(1, 1, 21, 18, constants.BLACK)
            self.moving_frames.append(image)
            image = sprite_sheet.get_image(25, 1, 18, 21, constants.BLACK)
            self.moving_frames.append(image)
            image = sprite_sheet.get_image(1, 26, 21, 18, constants.BLACK)
            self.moving_frames.append(image)
            image = sprite_sheet.get_image(26, 24, 18, 21, constants.BLACK)
            self.moving_frames.append(image)

        # Set the image the player starts with
        self.image = self.moving_frames[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

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

    def stop(self):
        #Release
        self.change_y = 0