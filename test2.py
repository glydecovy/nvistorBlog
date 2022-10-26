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
	cat_id 	= '5058812313'	
	bot.sendMessage(chat_id = cat_id, text=msgText)	
    
    
if __name__ == '__main__':
	telegram_token = sys.argv[1]

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
	###########################################################################################################
	# main 상단 banner
	table = bs.find('div', { 'class': 'home-group1' }) 
	title = '상단 BIG banner'

	data = []                            # 데이터를 저장할 리스트 생성
	result = []
	for img in table.find_all("img"):      
	    src = img["src"]
	    data.append([src]) 

	# 중복제거 : error 
	# tmp_data = set(data)
	# data = list(tmp_data)

	# 중복제거2
	for value in data:
	    if value not in result:
		result.append(value)
	# print(len(result))
	summary.append([title, len(result)]) 

	###########################################################################################################
	# 재구매율 상품
	table = bs.find('div', { 'class': 'home-group13-1' })  
	tmp_title = table.find('span', { 'class': 'group-head-copy' })
	# print(tmp_title)
	title = tmp_title.text 

	data = []                            # 데이터를 저장할 리스트 생성
	result = []
	for img in table.find_all("img"):      
	    src = img["data-src"]
	    data.append([src]) 
	#     print(src)

# 	# 중복제거2
# 	for value in data:
# 	    if value not in result:
# 		result.append(value)
	# print(result        )
	# print(len(result))
	summary.append([title, len(result)]) 

	###########################################################################################################
	# home-group19 : 극찬후기
	table = bs.find('div', { 'class': 'home-group19' })  
	tmp_title = table.find('div', { 'class': 'group-head-copy' })
	title = tmp_title.text

	data = []                            # 데이터를 저장할 리스트 생성
	result = []
	for img in table.find_all('div', { 'class': 'user-review-wrap' }) : 
	    src = img.text
	    data.append([src]) 
	#     print(src)

# 	# 중복제거2
# 	for value in data:
# 	    if value not in result:
# 		result.append(value)
	# print(result        )
	# print(len(result))
	summary.append([title, len(result)]) 
	###########################################################################################################
	# 추천 상품
	table = bs.find('div', { 'class': 'home-group13-2' })   
	tmp_title = table.find('span', { 'class': 'group-head-copy' })
	title = tmp_title.text

	data = []                            # 데이터를 저장할 리스트 생성
	result = []
	for img in table.find_all("img"):      
	    src = img["data-src"]
	    data.append([src]) 
	#     print(src)

# 	# 중복제거2
# 	for value in data:
# 	    if value not in result:
# 		result.append(value)
	# print(result        )
	# print(len(result))
	summary.append([title, len(result)]) 
	###########################################################################################################
	# home-group2
	table = bs.find('div', { 'class': 'home-group2' })  
	tmp_title = table.find('div', { 'class': 'group-head-copy' })
	title = tmp_title.text

	data = []                            # 데이터를 저장할 리스트 생성
	result = []
	for img in table.find_all("img"):      
	    src = img["src"]
	    data.append([src]) 
	#     print(src)

# 	# 중복제거2
# 	for value in data:
# 	    if value not in result:
# 		result.append(value)
	# print(result        )
	# print(len(result))
	summary.append([title, len(result)]) 


	###########################################################################################################
	# home-group18 : 신상품 : 상단 대표 이미지 포함
	table = bs.find('div', { 'class': 'home-group18' })  
	tmp_title = table.find('div', { 'class': 'group-head-copy' })
	title = tmp_title.text

	data = []                            # 데이터를 저장할 리스트 생성
	result = []
	for img in table.find_all("img"):      
	    src = img["data-src"]
	    data.append([src]) 
	#     print(src)

# 	# 중복제거2
# 	for value in data:
# 	    if value not in result:
# 		result.append(value)
	# print(result        )
	# print(len(result))
	summary.append([title, len(result)]) 
	###########################################################################################################
	# home-group18 :이번 주 BEST3 상품이에요
	table = bs.find('div', { 'class': 'home-group12' })  
	tmp_title = table.find('div', { 'class': 'group-head-copy' })
	title = tmp_title.text

	data = []                            # 데이터를 저장할 리스트 생성
	result = []
	for img in table.find_all("img", { 'class': 'thumb-type1'}):   
	    src = img["data-src"]
	    data.append([src]) 
	#     print(src)

	# webp 화일만 추출
	# tmp_data = [s for s in data if ".webp" in s]  
	# data = tmp_data

# 	# 중복제거2
# 	for value in data:
# 	    if value not in result:
# 		result.append(value)

	summary.append([title, len(result)]) 
	###########################################################################################################
	# home-group13 :극찬후기 상품
	table = bs.find('div', { 'class': 'home-group13' })  
	tmp_title = table.find('span', { 'class': 'group-head-copy' })
	title = tmp_title.text

	data = []                            # 데이터를 저장할 리스트 생성
	result = []
	for img in table.find_all("img", { 'class': 'thumb-type1'}):   
	    src = img["data-src"]
	    data.append([src]) 
	#     print(src)

	# webp 화일만 추출
	# tmp_data = [s for s in data if ".webp" in s]  
	# data = tmp_data

# 	# 중복제거2
# 	for value in data:
# 	    if value not in result:
# 		result.append(value)

	summary.append([title, len(result)]) 

	###########################################################################################################
	# home-group14:글라이득템, 코너 상단 big image 포함
	table = bs.find('div', { 'class': 'home-group14' })  
	tmp_title = table.find('div', { 'class': 'group-head-copy' })
	title = tmp_title.text

	data = []                            # 데이터를 저장할 리스트 생성
	result = []
	for img in table.find_all("img"):   
	    src = img["data-src"]
	    data.append([src]) 
	#     print(src)

# 	# 중복제거2
# 	for value in data:
# 	    if value not in result:
# 		result.append(value)

	summary.append([title, len(result)]) 
	###########################################################################################################
	# home-group7:고객님께 추천드려요
	table = bs.find('div', { 'class': 'home-group7' })  
	tmp_title = table.find('div', { 'class': 'group-head-copy' })
	title = tmp_title.text

	data = []                            # 데이터를 저장할 리스트 생성
	result = []
	for img in table.find_all("img", { 'class': 'thumb-type1'}):   
	    src = img["data-src"]
	    data.append([src]) 
	#     print(src)

# 	# 중복제거2
# 	for value in data:
# 	    if value not in result:
# 		result.append(value)

	summary.append([title, len(result)]) 
	###########################################################################################################
	# home-group11:냉동실 쟁여템 추천
	table = bs.find('div', { 'class': 'home-group11' })  
	tmp_title = table.find('div', { 'class': 'group-head-copy' })
	title = tmp_title.text

	data = []                            # 데이터를 저장할 리스트 생성
	result = []
	for img in table.find_all("img", { 'class': 'thumb-type1'}):   
	    src = img["data-src"]
	    data.append([src]) 
	#     print(src)

# 	# 중복제거2
# 	for value in data:
# 	    if value not in result:
# 		result.append(value)

	summary.append([title, len(result)]) 

	################################################[최종 LIST]################################################
	# print(summary)

	################################################[table 꾸미기]#############################################

# 	matplotlib.rcParams['font.family'] ='Malgun Gothic'
# 	matplotlib.rcParams['axes.unicode_minus'] =False
# 	matplotlib.font_manager._rebuild()

	df = pd.DataFrame(summary, columns=['corner', 'image_count'])
	df.set_index('corner',drop=True,inplace=True)
	print(df)

	cell_text = df.values
	colors = plt.cm.BuPu(np.linspace(0, 0.5, len(df.index)))
	columns = list(df.columns)
	rows = list(df.index)


	fig, ax =plt.subplots(1,1)

	ax.axis('tight')
	ax.axis('off')

	ax.table(cellText=df.values,colLabels=df.columns,rowLabels=df.index,loc="center")

	# plt.show()
# 	plt.savefig('20221021.png')  
	chk_df = df
	print(chk_df)
	print(type(chk_df.to_string()))
	print(chk_df.to_string())
	sDf = chk_df.to_string()
	try:
    		sendMsg(telegram_token, sDf)														
	except Exception as e:
		print("e:",e)   
