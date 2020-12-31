import os
import json

class ConfigExtractor:
    def __init__(self):
        with open(os.getcwd() + "/data/config.json") as configFile:
            self.config = json.load(configFile)
    
    def __getitem__(self, key):
        return self.config[key]