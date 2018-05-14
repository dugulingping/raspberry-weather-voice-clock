#!/usr/bin/python3.6
#-*-coding:utf-8 -*-
import requests
import json
import time 
import sys
reload(sys)
sys.setdefaultencoding('utf8')

jsonAPI = requests.get('https://www.sojson.com/open/api/weather/json.shtml?city=%E5%A4%A9%E6%B4%A5')
jsonAPI.encoding = 'utf-8'
json = jsonAPI.json()
#print json
if json['status'] == 200:
	weather = {
	'city' : json['city'],
	'shidu' : json['data']['shidu'],
	'aqi' : json['data']['forecast'][0]['aqi'],
	'high' : json['data']['forecast'][0]['high'],	
	'low' : json['data']['forecast'][0]['low'],
	'fengxiang' : json['data']['forecast'][0]['fx'],
	'fengli' : json['data']['forecast'][0]['fl'],
	'type' : json['data']['forecast'][0]['type'],
	'notice' : json['data']['forecast'][0]['notice']
	}
	timeclock = time.strftime('今天是%m月%d日，',time.localtime(time.time()))
	str = weather['type']+','+weather['high']+','+weather['low']+','+weather['fengxiang']+weather['fengli']
	str = "%s,湿度:%s,天气质量:%s。给主人一点温馨提示：%s" % (str,weather['shidu'],weather['aqi'],weather['notice'])
	print str
else:
	print 'error'
	print json['status']
