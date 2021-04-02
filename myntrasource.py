# https://www.myntra.com/amp/women-ethnic-wear
import requests
import random
import re
import json
from bs4 import BeautifulSoup as soup
from requests_html import HTMLSession
import urllib
import http.cookiejar, urllib.request as urllib2
import csv
import pandas

# site = 'https://www.myntra.com/amp/women-ethnic-wear'
site = 'https://www.myntra.com/amp/women-ethnic-wear?row-50&p=2'
hdr1 = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Referer': 'https://www.myntra.com/amp/women-ethnic-wear?row-50&p=2',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
hdr2 = {'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Referer': 'https://www.myntra.com/amp/women-ethnic-wear?row-50&p=2',
       'Connection': 'keep-alive'}
hdr3 = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Referer': 'https://www.myntra.com/amp/women-ethnic-wear?row-50&p=2',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
hdr4 = {'User-Agent': 'Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Referer': 'https://www.myntra.com/amp/women-ethnic-wear?row-50&p=2',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
hdr5 = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Referer': 'https://www.myntra.com/amp/women-ethnic-wear?row-50&p=2',
       'Connection': 'keep-alive'}
hdr = random.choice([hdr1,hdr2,hdr3,hdr4,hdr5])
req = urllib2.Request(site, headers=hdr)


cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
response = opener.open(req)
content = response.read()
# print(content)
response.close()

page_soup = soup(content,"html.parser")

xyz  = page_soup.findAll("div",{"class" : "productInfo"})
pqr  = page_soup.findAll("div",{"class" : "product"})

y = len(xyz)
# print(xyz)
# print(pqr)
print(type(xyz))
print(y)
diclist = []
dic={}
maindiv = page_soup.find_all('.product')

for div in pqr:
    productname = [x.text for x in div.select('.name')]
    # print(productname)
    price = [x.text for x in div.select('.price')]
    # print(price)
    pricediscounted = [x.text for x in div.select('.price-discounted')]
    # print(pricediscounted)
    # productlink = [x.attrs['href'] for x in div.select('')]
    # print(productlink)
    imagelink = [x.attrs['src'] for x in div.select('img')]
    # print(imagelink)
    # imagelink= div.findAll("img",{"class":"i-amphtml-element"})


    # dic = {'productname':productname,'price':price,'pricediscounted':pricediscounted}
    dic = {'productname':productname,'price':price,'pricediscounted':pricediscounted,'imagelink':imagelink}
    # dic = {'productname':productname,'price':price,'pricedicounted':pricediscounted,'prodctlink':productlink,'imagelink':imagelink,}
    
    diclist.append(dic)
    print(dic)

json_text = json.dumps(diclist,indent=4)
with open('myntrajsn.json', 'w') as json_file:
    json_file.write(json_text)
