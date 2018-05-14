#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
from aip import AipSpeech
import requests
import re
from bs4 import BeautifulSoup
import json
import time 
import sys
reload(sys)
sys.setdefaultencoding('utf8')
'''
作者：独孤伶俜
时间：2018.5.3
最后修改时间：2018.5.14 16:30
声明：本程序尊循GPL开源协议，意味着您可以自由的下载分发，但修改新增内容要遵循同样的协议，同时注明署名！
声明2：本程序作者不对任何商业和非商业内容负责，请知晓！

程序运行需网络通畅！
'''

def getweather(city):
	jsonAPI = requests.get('https://www.sojson.com/open/api/weather/json.shtml?city=' + city)
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
		str = timeclock + '今天' + weather['city'] + weather['type']+','+weather['high']+'，'+weather['low']+'，'+weather['fengxiang']+weather['fengli']
		str = "%s,湿度:%s,天气质量:%s。%s" % (str,weather['shidu'],weather['aqi'],weather['notice'])
		print str
		return str
	else:
		print 'error'
		print json['status']
		return '哎呀，我也不知道今天的天气啦！'

'''
用百度的AIP
把文字变成mp3文件
'''
def stringToMp3(strings):
    per=0
    strings_txt = '又是新的一天。主人起床呀～,懒虫～,起床咯～,死肥宅～,起床啦～。要上课啦！' 
    APPID = '11216646'
    APIKey = 'sW9uxIBmiFkq0iDdY2I4GOVT'
    SecretKey = '9966e70a6520218cf157def8c2005edc'
    aipSpeech = AipSpeech(APPID,APIKey,SecretKey)
    aipSpeech.setConnectionTimeoutInMillis(5000)
    aipSpeech.setSocketTimeoutInMillis(100000)

    result = aipSpeech.synthesis(strings_txt,'zh','1',\
                                {'vol':10,
                                'per':per,
                                'spd':4
})
    if not isinstance(result,dict):
        with open('test_tmp.mp3','wb') as f:
            f.write(result) 
            
    result = aipSpeech.synthesis(strings,'zh','1',\
                                {'vol':10,
                                'per':per,
                                'spd':4
})
    if not isinstance(result,dict):
        with open('test_tmp.mp3','ab') as f:
            f.write(result) 

#执行的主函数
def main():
	city = '天津'
	stringToMp3(getweather(city))
 
if __name__ == '__main__':
    main()
