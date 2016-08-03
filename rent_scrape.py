import re
import requests
from bs4 import BeautifulSoup
import cPickle as pickle
import send_email
import json


def rent_xingshan():
    session = requests.Session()
    headers = {"Accept": "application/json, text/javascript, */*",
               "Accept-Encoding": "gzip, deflate, sdch, br",
               "Accept-Language": "en-US,en;q=0.8", "Connection": "keep-alive",
               "Cookie": "PHPSESSID=71f9a9d297e5dd16c4a36fc1306a2542; urlJumpIp=1; urlJumpIpByTxt=%E5%8F%B0%E5%8C%97%E5%B8%82;",
               "Host": "rent.591.com.tw",
               "DNT": "1",
               "Referer": "https://rent.591.com.tw/map-index.html",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                             "like Gecko) Chrome/50.0.2661.102 Safari/537.36",
               "X-Requested-With": "XMLHttpRequest"}
    url_duli = "https://rent.591.com.tw/map-search.html?l11=1&l12=0&l21=17&l22=25.056744553050592&l23=121.57793898692476&l31=17&l32=25.056744553050592&l33=121.57793898692476&l41=25.052749924570147&l42=25.060739051331193&l43=121.57038588633884&l44=121.58549208751072&p11=0&p12=0&p13=0&p14=0&f0=2&f1=0&f2=0&f3=0&f4=0&f5=0&f6=undefined&f7=undefined&f8=undefined&rid=1&sid=&_=1468159318211"
    url_fenzhu = "https://rent.591.com.tw/map-search.html?l11=1&l12=0&l21=17&l22=25.056744553050592&l23=121.57793898692476&l31=17&l32=25.056744553050592&l33=121.57793898692476&l41=25.052749924570147&l42=25.060739051331193&l43=121.57038588633884&l44=121.58549208751072&p11=0&p12=0&p13=0&p14=0&f0=3&f1=0&f2=0&f3=0&f4=0&f5=0&f6=undefined&f7=undefined&f8=undefined&rid=1&sid=&_=1468159340424"
    url_zhengcheng = "https://rent.591.com.tw/map-search.html?l11=1&l12=0&l21=17&l22=25.056744553050592&l23=121.57793898692476&l31=17&l32=25.056744553050592&l33=121.57793898692476&l41=25.052749924570147&l42=25.060739051331193&l43=121.57038588633884&l44=121.58549208751072&p11=0&p12=0&p13=0&p14=0&f0=1&f1=0&f2=1&f3=0&f4=0&f5=0&f6=undefined&f7=undefined&f8=undefined&rid=1&sid=&_=1468159224728"
    url_list = [url_duli, url_fenzhu, url_zhengcheng]

    try:
        with open('591_xingshan.pk', 'rb') as input:
            rent_list = pickle.load(input)
    except:
        rent_list = list()

    old_length = len(rent_list)

    for url in url_list:
        req = session.get(url, headers=headers)

        bsObj = BeautifulSoup(req.text, "lxml")
        if not json.loads(bsObj.text)['ware']:
            continue
        href_list = bsObj.find_all("a", href=re.compile('rent.*?html'))

        for i in href_list:
            if i['href'][2:-2] not in rent_list:
                rent_list.append(i['href'][2:-2])

    rent_main = "https://rent.591.com.tw/"
    if old_length != len(rent_list):
        with open('591_xingshan.pk', 'wb') as output:
            pickle.dump(rent_list, output, -1)
        if not old_length:
            send_email.send_mail('xingshan', "\n\r" + rent_main + ("\n\r" + rent_main).join(
                    rent_list))
        else:
            send_email.send_mail('xingshan', "\n\r" + rent_main + ("\n\r" + rent_main).join(
                    rent_list[old_length:]))

    print "591 xingshan scrape done"


def rent_neihulu():
    session = requests.Session()
    headers = {"Accept": "application/json, text/javascript, */*",
               "Accept-Encoding": "gzip, deflate, sdch, br",
               "Accept-Language": "en-US,en;q=0.8", "Connection": "keep-alive",
               "Cookie": "PHPSESSID=71f9a9d297e5dd16c4a36fc1306a2542; urlJumpIp=1; urlJumpIpByTxt=%E5%8F%B0%E5%8C%97%E5%B8%82;",
               "Host": "rent.591.com.tw",
               "DNT": "1",
               "Referer": "https://rent.591.com.tw/map-index.html",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                             "like Gecko) Chrome/50.0.2661.102 Safari/537.36",
               "X-Requested-With": "XMLHttpRequest"}
    url_duli_1 = "https://rent.591.com.tw/map-search.html?l11=1&l12=0&l21=18&l22=25.085143&l23=121.5613085&l31=18&l32=25.085143&l33=121.5613085&l41=25.083061140971203&l42=25.087224823618634&l43=121.55752926749801&l44=121.56508773250198&p11=0&p12=0&p13=0&p14=0&f0=2&f1=2&f2=0&f3=0&f4=0&f5=0&f6=undefined&f7=undefined&f8=undefined&rid=1&sid=&_=1470029782553"
    url_fenzhu_1 = "https://rent.591.com.tw/map-search.html?l11=1&l12=0&l21=18&l22=25.085143&l23=121.5613085&l31=18&l32=25.085143&l33=121.5613085&l41=25.083061140971203&l42=25.087224823618634&l43=121.55752926749801&l44=121.56508773250198&p11=0&p12=0&p13=0&p14=0&f0=3&f1=2&f2=0&f3=0&f4=0&f5=0&f6=undefined&f7=undefined&f8=undefined&rid=1&sid=&_=1470029840843"
    url_zc_1 = "https://rent.591.com.tw/map-search.html?l11=1&l12=0&l21=18&l22=25.085143&l23=121.5613085&l31=18&l32=25.085143&l33=121.5613085&l41=25.083061140971203&l42=25.087224823618634&l43=121.55752926749801&l44=121.56508773250198&p11=0&p12=0&p13=0&p14=0&f0=1&f1=2&f2=1&f3=0&f4=0&f5=0&f6=undefined&f7=undefined&f8=undefined&rid=1&sid=&_=1470029864451"

    url_duli_2 = "https://rent.591.com.tw/map-search.html?l11=1&l12=0&l21=18&l22=25.085143&l23=121.5613085&l31=18&l32=25.085143&l33=121.5613085&l41=25.083061140971203&l42=25.087224823618634&l43=121.55752926749801&l44=121.56508773250198&p11=0&p12=0&p13=0&p14=0&f0=2&f1=3&f2=0&f3=0&f4=0&f5=0&f6=undefined&f7=undefined&f8=undefined&rid=1&sid=&_=1470029954363"
    url_fenzhu_2 = "https://rent.591.com.tw/map-search.html?l11=1&l12=0&l21=18&l22=25.085143&l23=121.5613085&l31=18&l32=25.085143&l33=121.5613085&l41=25.083061140971203&l42=25.087224823618634&l43=121.55752926749801&l44=121.56508773250198&p11=0&p12=0&p13=0&p14=0&f0=3&f1=3&f2=0&f3=0&f4=0&f5=0&f6=undefined&f7=undefined&f8=undefined&rid=1&sid=&_=1470029968645"
    url_zc_2 = "https://rent.591.com.tw/map-search.html?l11=1&l12=0&l21=18&l22=25.085143&l23=121.5613085&l31=18&l32=25.085143&l33=121.5613085&l41=25.083061140971203&l42=25.087224823618634&l43=121.55752926749801&l44=121.56508773250198&p11=0&p12=0&p13=0&p14=0&f0=1&f1=3&f2=1&f3=0&f4=0&f5=0&f6=undefined&f7=undefined&f8=undefined&rid=1&sid=&_=1470029905921"
    url_list = [url_duli_1, url_fenzhu_1, url_zc_1, url_duli_2, url_fenzhu_2, url_zc_2]

    try:
        with open('591_neihulu_CN.pk', 'rb') as input:
            rent_list = pickle.load(input)
    except:
        rent_list = list()

    old_length = len(rent_list)

    for url in url_list:
        req = session.get(url, headers=headers)

        bsObj = BeautifulSoup(req.text, "lxml")
        if not json.loads(bsObj.text)['ware']:
            continue
        href_list = bsObj.find_all("a", href=re.compile('rent.*?html'))

        for i in href_list:
            if i['href'][2:-2] not in rent_list:
                rent_list.append(i['href'][2:-2])

    rent_main = "https://rent.591.com.tw/"
    if old_length != len(rent_list):
        with open('591_neihulu_CN.pk', 'wb') as output:
            pickle.dump(rent_list, output, -1)
        if not old_length:
            send_email.send_mail_CN('neihulu', "\n\r" + rent_main + ("\n\r" + rent_main).join(
                    rent_list))
        else:
            send_email.send_mail_CN('neihulu', "\n\r" + rent_main + ("\n\r" + rent_main).join(
                    rent_list[old_length:]))

    print "591 neihulu scrape done"
