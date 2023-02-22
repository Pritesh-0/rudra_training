import pygame
import time
pygame.init()

done = False
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
while not done:
    pygame.event.get()
    joystick=joysticks[0]
    b1,b2,b3 = joystick.get_button(0),joystick.get_button(2),joystick.get_button(4)
    print("b1: ",b1)
    print("b2: ",b2)
    print("b3: ",b3)
    time.sleep(0.5)
