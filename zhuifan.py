#!*-* coding: utf-8 *-*

# 追番需要使用动漫花园的RSS源, 追踪并跟新目标新番

BASE_URL = "https://share.dmhy.org/topics/rss/rss.xml?keyword="

KEY_WORD = [
    "一拳"
]

import feedparser
import pprint

def handle():
    for key in KEY_WORD:
        feed = feedparser.parse(BASE_URL + key)
        for item in feed.entries:
            yield item.title

import ipdb;ipdb.set_trace()