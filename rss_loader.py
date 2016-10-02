#!/usr/bin/env python3

import feedparser
import listparser
import sqlite3


def parse_feed(feed_url):
    feed = feedparser.parse(feed_url)
    connection = sqlite3.connect('db/sent_news.db')
    filtered_entries = list(filter(lambda entry: is_already_sent(entry, connection.cursor()), feed.entries))
    mark_as_sent(filtered_entries, connection)
    connection.commit()
    connection.close()
    return filtered_entries


def news():
    feed_list = listparser.parse('config/subs.opml').feeds
    filtered_list = []
    for feed in feed_list:
        filtered_list += parse_feed(feed.url)
    return filtered_list


def is_already_sent(entry, connection):
    query = 'SELECT count(*) from sent_news where url = (?)'
    return connection.execute(query, [entry.link]).fetchone()[0] == 0


def mark_as_sent(entries, connection):
    query = 'INSERT INTO sent_news (url) VALUES (?)'
    import_data = list(map(lambda entry: [entry.link], entries))

    connection.executemany(query, import_data)
