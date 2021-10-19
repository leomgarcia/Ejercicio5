# Import a library of functions called 'pygame'

import pygame
from main_functions import *

# Initialize the game engine
pygame.init()

#call main routine
size = [1300, 600] # Define size of windows
hight = int(input("Alto de la ventana:"))
wide = int(input("Ancho de la ventana:"))
size[1] = hight
size[0] = wide
GREEN (0, 255, 0)
title = input("Asignar titulo:")
main2(size, title, GREEN)

