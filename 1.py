#!/usr/bin/python3.6
#-*-coding:utf-8 -*-
import requests
import json
import time 

date = time.strftime('%Y%m%d',time.localtime(time.time()))
file = open("weather.log", "r")
jsonj = json.load(file)
file.close()
#print(jsonj)

	
city ='西青' #在这里修改你的所在城市，可以精确到区，县，市

juheurl = 'http://v.juhe.cn/weather/index?cityname='+city+'&key=*******************************'	#这里是聚合数据api 你需要申请一个key

freeurl = 'https://www.sojson.com/open/api/weather/json.shtml?city='+city
#print(jsonj)
if (jsonj['date'] == date and jsonj['city'] == city and jsonj['code'] == '200'):
	print('不需要重新请求 今天：' + date + city)
	exit()
	
jsonAPI = requests.get(freeurl)
jsonAPI.encoding = 'utf-8'
jsonj = jsonAPI.json()

#判断获取的数据
if jsonj['status'] == 200:
	jsonj['url_type'] = 'free'
	jsonj['date'] = date
	jsonj['city'] = city
	#写入文件
	file = open("weather.log", "w")
	file.write(json.dumps(jsonj))
	file.close()
else:
	jsonAPI = requests.get(juheurl)
	jsonAPI.encoding = 'utf-8'
	jsonj = jsonAPI.json()
	if (jsonj['resultcode'] == '200'):
		jsonj['url_type'] = 'juhe'
		jsonj['date'] = date
		jsonj['city'] = city
		jsonj['code'] = str(jsonj['resultcode'])
		#写入文件
		file = open("weather.log", "w")
		file.write(json.dumps(jsonj))
		file.close()
	else:
		jsonj['url_type'] = 'error'
		jsonj['date'] = date
		jsonj['city'] = city
		jsonj['code'] = str(jsonj['resultcode'])
		file = open("weather.log", "w")
		file.write(json.dumps(jsonj))
		file.close()
		
		