#!/usr/bin/env python3

import yaml
import telegram

with open('config.yml', 'r') as configfile:
    config = yaml.load(configfile)

bot = telegram.Bot(token=config['telegram']['api_token'])
