import time
from selenium import webdriver
from itertools import count
from bs4 import BeautifulSoup
import pandas as pd             # pandas 라이브러리
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

import os,sys
import requests
import xml.etree.ElementTree as ET
import datetime
import telegram 
from pytz import timezone

def getToDay():
	return KST.strftime("%Y%m%d")
def getNowTime():
	return KST.strftime("%Y년%m월%d일 %H시%M분")

def sendMsg(telegram_token, msgText):
	bot 	= telegram.Bot(token = telegram_token)
# 	cat_id 	= '-1001187429712'	
	bot.sendMessage(chat_id = cat_id, text=msgText)	
    
    
if __name__ == '__main__':
	telegram_token = sys.argv[1]
	cat_id 	= sys.argv[2]
	
	# python3 에서 sys 안됨
	# import sys
	# reload(sys)
	# sys.setdefaultencoding('utf-8')
	#-*- coding:utf-8 -*-

	url = 'https://m.glyde.co.kr/ui/display/mainPage'

	# wd = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
	options = webdriver.ChromeOptions()
	options.add_argument("start-maximized")
	options.add_argument("lang=ko_KR")
	options.add_argument('headless')
	options.add_argument('window-size=1920x1080')
	options.add_argument("disable-gpu")
	options.add_argument("--no-sandbox")	

	# chrome driver
	wd = webdriver.Chrome('chromedriver', options=options)
	wd.implicitly_wait(3)    

	wd.get(url)
	time.sleep(5)
	html = wd.page_source
	bs = BeautifulSoup(html, 'html.parser')

	summary =[]
# 	error_flag : false 가 정상 = 모든 이미지가 3개 이상인 경우
	error_flag = False 

    soup = Soup(html)
    divs = soup.find("div", {"class": "home-group"}, partial=True)
    # [div.text for div in divs]

    for index, value in enumerate(divs):
#         index 12, 글라이드스토리 제외
        if index == 12 : continue
#         print(index, value.text)
#         print(dir(value))
#         print(value.attrs)
        tmp = value.attrs
        
        ###########################################################################################################
        grpNm = tmp.get('class')        
        table = bs.find('div', { 'class': grpNm }) 
        title = tmp.get('id')
#         print("title:", title)
    
        tmp_table = bs.find('div', { 'class': grpNm })  
        tmp_title = tmp_table.find('div', { 'class': 'group-head-copy' })
        
        try:
            t_title = tmp_title.text
# 값이 없으면
        except Exception as e:
            t_title = table.find('span', { 'class': 'group-head-copy' })   
            try:
                t_title = tmp_title.text   
            except Exception as e:
                t_title = title
                
        title = t_title
        print("tmp_title:", t_title)

        data = []                            # 데이터를 저장할 리스트 생성
        result = []
        if grpNm == 'home-group1':
            tmp_img = table.find_all("img")
            tmp_src = "src"
        elif grpNm == 'home-group13-1':
            tmp_img = table.find_all("img")
            tmp_src = "data-src"
        elif grpNm == 'home-group19':
            tmp_img = table.find_all('div', { 'class': 'user-review-wrap' })
            
        elif grpNm == 'home-group13-2':
            tmp_img = table.find_all("img")
            tmp_src = "data-src"
            
        elif grpNm == 'home-group2':
            tmp_img = table.find_all("img")
            tmp_src = "src"
            
        elif grpNm == 'home-group18':
            tmp_img = table.find_all("img")
            tmp_src = "data-src"
            
        elif grpNm == 'home-group12':
            tmp_img = table.find_all("img", { 'class': 'thumb-type1'})
            tmp_src = "data-src"
            
        elif grpNm == 'home-group13':
            tmp_img = table.find_all("img", { 'class': 'thumb-type1'})
            tmp_src = "data-src"
            
        elif grpNm == 'home-group14':
            tmp_img = table.find_all("img")
            tmp_src = "data-src"
            
        elif grpNm == 'home-group7':
            tmp_img = table.find_all("img", { 'class': 'thumb-type1'})
            tmp_src = "data-src"
            
        elif grpNm == 'home-group11':
            tmp_img = table.find_all("img", { 'class': 'thumb-type1'})
            tmp_src = "data-src"      
            
        elif grpNm == 'home-group15':
            tmp_img = table.find_all("img", { 'class': 'thumb-type1'})
            tmp_src = "data-src"            
            
        else:
            tmp_img = table.find_all("img")
            tmp_src = "src"
        
        
        if grpNm == 'home-group19':
            for img in tmp_img : 
                src = img.text
                data.append([src])            
        else :
            
            for img in tmp_img:      
                src = img[tmp_src]    
                data.append([src]) 
        
        # 중복제거2
        for value in data:
            if value not in result:result.append(value)
        summary.append([title, len(result)]) 

    print("###########################################################################################################")
    print(summary)

    df = pd.DataFrame(summary, columns=['corner', 'image_count'])
    df.set_index('corner',drop=True,inplace=True)
#     print(df)
    df.reset_index(inplace=True)
    sDf = sendingForm(df)
    t= tabulate(df, headers='keys', tablefmt='plain', showindex=False, numalign='right' )
    print(t)
    try:
      sendMsg(telegram_token, t)
    except Exception as e:
      print("e:",e)   
