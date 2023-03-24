import pygame
import sys
import random
import os

def load_image(name):
 os.chdir('../img')
 image = pygame.image.load(name)
 os.chdir('../src')
 return image

class Enemy(pygame.sprite.Sprite):
 def __init__(self, x, y, v1, v2, name, bx, by):
     super().__init__()
     self.images = []
     self.images.append(load_image(name))

     self.index = 0
     self.image = self.images[self.index]
     self.rect = pygame.Rect(0, 0, bx, by)

     self.rect.y = y
     self.rect.x = x

     # Set speed vector
     self.change_x = v1
     self.change_y = v1
     
     self.caught = False

 def update(self):
     self.rect.x += self.change_x
     self.rect.y += self.change_y
        
 def stop(self):
      #called when game is paused
     self.change_x = 0
     self.change_y = 0
        
 def go(self):
     self.change_x = v1
     self.change_y = v2    