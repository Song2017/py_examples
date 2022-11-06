#!/usr/bin/env python
# encoding: utf-8
"""
Author: Ben
Mail: nghuyong@163.com
Created Time: 2022/10/30
"""
import json
from scrapy import Spider
from scrapy.http import Request
from bs4 import BeautifulSoup


class JokeSpider(Spider):
    """
    微博用户信息爬虫
    """
    name = "joke_spider"

    def start_requests(self):
        """
        爬虫入口
        """
        with open('./data/duanzi_urls.json') as f:
            urls = json.loads(f.read())
        for url in urls:
            yield Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        """
        网页解析
        """
        resp = response
        jokes = []
        # data = json.loads(response.text)
        selector = BeautifulSoup(resp.text)
        jokes.append(selector.find("em", {"id": "publish_time"}).getText())
        items = selector.findAll('section', {"data-tools": "135编辑器"})
        jokes.extend([i.text for i in items])
        if not items:
            items = selector.findAll('p', {"class": None, "style": None})[:-1]
            text = ''
            for item in items:
                if item.text != '':
                    text += item.text
                else:
                    jokes.append(text)
                    text = ''
        # selector.xpath("//section[@data-tools='135编辑器']/section/section/span/text()")[0]
        # yield Request(url, callback=self.parse_detail, meta={'item': item})
        with open("./data/jokes2.json", "a+") as f:
            f.write(json.dumps(jokes, ensure_ascii=False))

    @staticmethod
    def parse_detail(response):
        """
        解析详细数据
        """
        item = response.meta['item']
        data = json.loads(response.text)['data']
        item['birthday'] = data.get('birthday', '')
        if 'created_at' not in item:
            item['created_at'] = data.get('created_at', '')
        item['desc_text'] = data.get('desc_text', '')
        item['ip_location'] = data.get('ip_location', '')
        item['sunshine_credit'] = data.get('sunshine_credit', {}).get('level',
                                                                      '')
        item['label_desc'] = [label['name'] for label in
                              data.get('label_desc', [])]
        if 'company' in data:
            item['company'] = data['company']
        if 'education' in data:
            item['education'] = data['education']
        yield item
