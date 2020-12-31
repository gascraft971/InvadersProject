import pygame
from classes import Scene, Level, config

# Set up the config class to import stuff from the config.json file
global CONFIG
CONFIG = config.ConfigExtractor()

pygame.init()
pygame.font.init()

if __name__ == "__main__":
    scene = Scene.Scene(CONFIG)
    scene.main()