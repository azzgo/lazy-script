#!*-* coding: utf-8 *-*

# 追番需要使用动漫花园的RSS源, 追踪并跟新目标新番

BASE_URL = "https://share.dmhy.org/topics/rss/rss.xml?keyword="

KEY_WORD = [
    "一拳"
]

import feedparser
import pickle
import os


def handle():
    for key in KEY_WORD:
        feed = feedparser.parse(BASE_URL + key)
        for item in feed.entries:
            yield item.title

record_hash = dict()

if os.path.isfile("./zhuifan.pickle"):
    open("./zhuifan.pickle") as file:
        record_hash = pickle.load(file)

for key in KEY_WORD:
    record = record_hash.get(key, 0)
    # 如何查询到最新的番种大于记录项, 启动下载, 否则暂停
    # TODO
