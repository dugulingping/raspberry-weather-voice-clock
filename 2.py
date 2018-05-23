import json
import time

def get_weather_json(jsonj):
	date = time.strftime('%Y%m%d',time.localtime(time.time()))
	if (jsonj['date'] == date):
		if jsonj['url_type'] == 'juhe':
			weather = {
				'code' : '200',
				'date' : jsonj['date'],
				'url_type' : jsonj['url_type'],
				'city' : jsonj['result']['today']['city'],
				'aqi' : jsonj['result']['today']['comfort_index'],
				'weather_info' : jsonj['result']['today']['temperature'],
				'fengli' : jsonj['result']['today']['wind'],
				'type' : jsonj['result']['today']['weather'],
				'qingkuang' : jsonj['result']['today']['dressing_index'],
				'notice' : jsonj['result']['today']['dressing_advice']
			}
	
		elif jsonj['url_type'] == 'free':
			weather = {
				'code' : '200',
				'date' : jsonj['date'],
				'url_type' : jsonj['url_type'],
				'city' : jsonj['city'],
				'shidu' : jsonj['data']['shidu'],
				'aqi' : jsonj['data']['forecast'][0]['aqi'],
				'high' : jsonj['data']['forecast'][0]['high'],	
				'low' : jsonj['data']['forecast'][0]['low'],
				'fengxiang' : jsonj['data']['forecast'][0]['fx'],
				'fengli' : jsonj['data']['forecast'][0]['fl'],
				'type' : jsonj['data']['forecast'][0]['type'],
				'notice' : jsonj['data']['forecast'][0]['notice']
			}
		else:
			weather = {
				'code' : jsonj['resultcode'],
				'date' : jsonj['date'],
				'errorinfo' : '哎呀，独小酱也不知道今天的天气啦！'
			}
	else:
		weather = {
			'code' : jsonj['resultcode'],
			'date' : jsonj['date'],
			'errorinfo' : "哎呀，天气数据过期啦，请重新获取"
			}
	return weather


def read_json_file():
	file = open("weather.log", "r")
	jsonj = json.load(file)
	file.close()
	#print(jsonj)
	return jsonj

def write_json_file(jsonj):
	file = open("weather_jian.log", "w")
	file.write(json.dumps(jsonj))
	file.close()

def get_weather_info(weather):
	if weather['url_type'] == 'free':
		timeclock = time.strftime('今天是%m月%d日，',time.localtime(time.time()))
		temp = timeclock + '今天' + weather['city'] + weather['type']+',' + weather['high'] + '，'+weather['low']+'，'+weather['fengxiang']+weather['fengli']
		str = [temp,]
		temp = "湿度: %s,天气质量:%s。%s" % (weather['shidu'],weather['aqi'],weather['notice'])
		str.append(temp)
	elif weather['url_type'] == 'juhe':
		#juhe
		timeclock = time.strftime('今天是%m月%d日，',time.localtime(time.time()))
		str = [(timeclock + '今天' + weather['city'] + weather['type']+ ',温度：'+ weather['weather_info'] + ',' +weather['fengli']),]
		str.append(('今天天气' + weather['qingkuang'] +'。' + weather['notice']))
	return str

def main():
	weatherjosn = read_json_file()
	#print(weatherjson)
	weather = get_weather_json(weatherjosn)
	str = get_weather_info(weather)
	weather['s1'] = str[0]
	weather['s2'] = str[1]
	write_json_file(weather)
	print(weather['s1'],weather['s2'])

if __name__ == '__main__':
	main()
	
	
	
	
	
	
	