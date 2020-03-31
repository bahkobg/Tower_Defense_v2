import pygame

enemy_1 = [pygame.image.load('assets/enemies/1/' + str(x) + '.png') for x in range(1, 11)]
enemy_2 = [pygame.image.load('assets/enemies/2/' + str(x) + '.png') for x in range(1, 11)]
enemy_3 = [pygame.image.load('assets/enemies/3/' + str(x) + '.png') for x in range(1, 11)]
enemy_4 = [pygame.image.load('assets/enemies/4/' + str(x) + '.png') for x in range(1, 11)]
enemy_5 = [pygame.image.load('assets/enemies/5/' + str(x) + '.png') for x in range(1, 11)]

towers = [pygame.image.load('assets/towers/1/' + str(x) + '.png') for x in range(1,7)]