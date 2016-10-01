#!/usr/bin/env python3

import feedparser

url = "http://kanobu.ru/rss/news.xml"

feed = feedparser.parse(url)

def parse_feed(feed_url):
    for post in feed.entries:
        print(post.link)
parse_feed(url)
