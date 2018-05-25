#!/usr/bin/python36
# -*- coding: utf-8 -*-
from aip import AipSpeech
import requests
import re
from bs4 import BeautifulSoup
import json
import time 

'''
作者：独孤伶俜
时间：2018.5.3
最后修改时间：2018.5.23 11:30
声明：本程序尊循GPL开源协议，意味着您可以自由的下载分发，但修改新增内容要遵循同样的协议，同时注明署名！
声明2：本程序作者不对任何商业和非商业内容负责，请知晓！

程序运行需网络通畅！
'''

def get_weather_jian():
	file = open("weather_jian.log", "r")
	jsonj = json.load(file)
	file.close()
	str = [jsonj['s1'],jsonj['s2'],]
	#print(str)
	return str


'''
用百度的AIP
把文字变成mp3文件
这里用了百度语音的api  你需要申请key
'''
def stringToMp3(strings):
    per=0
    strings_txt = '又是新的一天。主人起床呀,懒虫,起床咯,死肥宅,起床啦。要上课啦！' 
    print(strings[0],strings[1])
    APPID = '******'
    APIKey = '*******'
    SecretKey = '***********************'
    aipSpeech = AipSpeech(APPID,APIKey,SecretKey)
    aipSpeech.setConnectionTimeoutInMillis(5000)
    aipSpeech.setSocketTimeoutInMillis(100000)

    result = aipSpeech.synthesis(strings_txt,'zh','1',\
                                {'vol':10,
                                'per':'0',
                                'spd':5
					})
    if not isinstance(result,dict):
        with open('test_tmp.mp3','wb') as f:
            f.write(result)
     
    print(dict)
    result = aipSpeech.synthesis(strings[0],'zh','1',\
                                {'vol':10,
                                'per':'0',
                                'spd':6
					})
    if not isinstance(result,dict):
        with open('test_tmp.mp3','ab') as f:
            f.write(result) 
   
    print(dict)
    result = aipSpeech.synthesis(strings[1],'zh','1',\
                                {'vol':10,
                                'per':'0',
                                'spd':6
					})
    if not isinstance(result,dict):
        with open('test_tmp.mp3','ab') as f:
            f.write(result) 

    print(dict)


#执行的主函数
def main():
	stringToMp3(get_weather_jian())
 
if __name__ == '__main__':
    main()
