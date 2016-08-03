# coding=utf-8
import requests
from bs4 import BeautifulSoup
import json


def rent_duanzu():
    session = requests.Session()
    headers = {"Accept": "application/json, text/javascript, */*",
               "Accept-Encoding": "gzip, deflate, sdch, br",
               "Accept-Language": "en-US,en;q=0.8",
               "Connection": "keep-alive",
               "Cookie": "PHPSESSID=71f9a9d297e5dd16c4a36fc1306a2542; urlJumpIp=1; urlJumpIpByTxt=%E5%8F%B0%E5%8C%97%E5%B8%82;",
               "Host": "rent.591.com.tw",
               "DNT": "1",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:46.0) Gecko/20100101 "
                             "Firefox/46.0",
               "Referer": "https://rent.591.com.tw",
               "X-Requested-With": "XMLHttpRequest"}
    url = "https://rent.591.com.tw/index.php?module=search&action=rslist&is_new_list=1&type=1&searchtype=1&region=1&orderType=desc&listview=img&keywords=短租"
    url2 = "https://rent.591.com.tw/index.php?module=search&action=rslist&is_new_list=1&type=1&searchtype=1&region=1&orderType=desc&listview=img&keywords=短租&firstRow=0"
    req = session.get(url, headers=headers)
    # bsObj = BeautifulSoup(req.text, "lxml")
    print json.loads(req.text)
    # print json.loads(bsObj.text)['count']

rent_duanzu()
