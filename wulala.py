# -*- coding: utf-8 -*-
from aip import AipSpeech
import requests
import re
from bs4 import BeautifulSoup
import time
'''
作者：独孤伶俜
时间：2018.5.3
最后修改时间：2018.5.10 16:30
声明：本程序尊循GPL开源协议，意味着您可以自由的下载分发，但修改新增内容要遵循同样的协议，同时注明署名！
声明2：本程序作者不对任何商业和非商业内容负责，请知晓！

程序运行需网络通畅！

爬取天气网-天津西青
http://www.weather.com.cn/weather/101030500.shtml
'''
def getHtmlText(url,code='utf-8'):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ''
def makeSoup(html):
    wstr = ''
    if html == '':
        return '哎呀~今天我也不知道天津天气了'
    else:
        soup = BeautifulSoup(html,'html.parser')
        soup1 = soup.find_all('li',attrs = {'class':'on'})[1]
        str1 = re.findall(r'>(.*)</',str(soup1))
        b = ''
        try:
            slist = re.findall(r'^(.*)</span>(.*)<i>(.*)$',str1[4])
            for x in range(len(slist[0])):
                b += slist[0][x]
        except:
            b = str1[4]
        if '/' in b:
            b = b.replace('/','-')
	#print(b)
	str1[0] = time.strftime('今天是%Y年%m月%d日，',time.localtime(time.time()))
        str1[4] = '，今天天津的温度是，'+b+'，然后：'
        #print(str1[4])
        str1[6] = '小风风是'+str1[6]
        print(str1[6])
	for i in str1:
            if i != '':
                wstr = wstr +i
        if '雨' in wstr:
            wstr += '今天别忘记带雨伞哦！'
        print(wstr)
        return wstr
'''
用百度的AIP
把文字变成mp3文件
'''
def stringToMp3(strings):
    per=4
    strings_txt = '又是新的一天。主人起床呀～,懒虫～,起床啊～,死肥宅～,起床啦～。要上课啦！' 
    APPID = '11216646'
    APIKey = 'sW9uxIBmiFkq0iDdY2I4GOVT'
    SecretKey = '9966e70a6520218cf157def8c2005edc'
 
    aipSpeech = AipSpeech(APPID,APIKey,SecretKey)
    aipSpeech.setConnectionTimeoutInMillis(5000)
    aipSpeech.setSocketTimeoutInMillis(100000)
    result = aipSpeech.synthesis(strings_txt,'zh','1',\
                                {'vol':10,
                                'per':per,
                                'spd':5

})
    if not isinstance(result,dict):
        with open('test_tmp.mp3','wb') as f:
            f.write(result) 

    result = aipSpeech.synthesis(strings,'zh','1',\
                                {'vol':10,
                                'per':per,
                                'spd':3

})
    if not isinstance(result,dict):
        with open('test_tmp.mp3','ab') as f:
            f.write(result)

    strings_txt = '。天气报完了，再不起床就要迟到啦。再不起床就不喜欢你啦。'
    result = aipSpeech.synthesis(strings_txt,'zh','1',\
                                {'vol':10,
                                'per':per,
                                'spd':5

})
    if not isinstance(result,dict):
        with open('test_tmp.mp3','ab') as f:
            f.write(result)
#执行的主函数
def main():
    url = 'http://www.weather.com.cn/weather/101030100.shtml'
    html=getHtmlText(url)
    stringToMp3(makeSoup(html))
 
if __name__ == '__main__':
    main()
