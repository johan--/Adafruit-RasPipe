#!/usr/bin/env python

import sys
import random

import pygame
import os

os.putenv('SDL_FBDEV', '/dev/fb1')

text_color = pygame.Color(0, 0, 0)
bg_color = pygame.Color(255, 255, 255)

pygame.init()
screen = pygame.display.set_mode([320, 240])
screen.fill(bg_color)

pygame.display.update()
