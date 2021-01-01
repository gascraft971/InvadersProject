import pygame
import os
from classes import Scene, config

# Set up the config class to import stuff from the config.json file
global CONFIG
CONFIG = config.ConfigExtractor()

pygame.init()
pygame.font.init()
pygame.joystick.init()

if __name__ == "__main__":
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    scene = Scene.Scene(CONFIG)
    scene.main()