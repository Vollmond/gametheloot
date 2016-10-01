#!/usr/bin/env python3

import yaml
import telegram
import rss_loader
from yattag import Doc

from telegram.ext import (Updater, Job)

with open('config.yml', 'r') as configfile:
    config = yaml.load(configfile)

bot = telegram.Bot(token=config['telegram']['api_token'])
updater = Updater(token=config['telegram']['api_token'])

def check_news_callback(bot, job):
    for article in rss_loader.news
        bot.send_message(chat_id=config['telegram']['channel_id'],
        text: pepare_article(article), parse_mode: 'html')

def prepare_article(article):
    tag = Doc().tagtext()
    with tag('a', href=article.link):
        article.title

updater.job_queue.put(Job(check_news_callback, 60.0))
# bot.sendMessage(chat_id=config['telegram']['channel_id'], text='Hello World!')

updater.start_polling()
