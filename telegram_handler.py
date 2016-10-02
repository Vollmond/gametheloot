#!/usr/bin/env python3

import yaml
import telegram
import rss_loader
from yattag import Doc
from telegram.ext import (Updater, Job)
fake_send = False


with open('config/config.yml', 'r') as configfile:
    config = yaml.load(configfile)

bot = telegram.Bot(token=config['telegram']['api_token'])
updater = Updater(token=config['telegram']['api_token'])


def check_news_callback(bot, job):
    for article in rss_loader.news():
        if fake_send:
            print(prepare_article(article))
        else:
            bot.send_message(chat_id=config['telegram']['channel_id'],
                             text=prepare_article(article), parse_mode='html')

def prepare_article(article):
    doc, tag, text = Doc().tagtext()
    with tag('a', href=article.link):
        text(article.title)
    return doc.getvalue()

updater.job_queue.put(Job(check_news_callback, 10.0))

updater.start_polling()
