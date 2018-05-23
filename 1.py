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

if jsonj['date'] == date:
	print('不需要重新请求 今天：' + date)
	exit()
	
city ='西青' #在这里修改你的所在城市，可以精确到区，县，市

juheurl = 'http://v.juhe.cn/weather/index?cityname='+city+'&key=youkey'	#这里是聚合数据api 你需要申请一个key

freeurl = 'https://www.sojson.com/open/api/weather/json.shtml?city='+city

jsonAPI = requests.get(freeurl)
jsonAPI.encoding = 'utf-8'
jsonj = jsonAPI.json()
#print(type(jsonj['status']))

#判断获取的数据
if jsonj['status'] == 200:
	jsonj['url_type'] = 'free'
	jsonj['date'] = date
	#写入文件
	file = open("weather.log", "w")
	file.write(json.dumps(jsonj))
	file.close()
else:
	jsonAPI = requests.get(juheurl)
	jsonAPI.encoding = 'utf-8'
	jsonj = jsonAPI.json()
	jsonj['url_type'] = 'juhe'
	jsonj['date'] = date
	#写入文件
	file = open("weather.log", "w")
	file.write(json.dumps(jsonj))
	file.close()
