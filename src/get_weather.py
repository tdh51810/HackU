# -*- coding: utf-8 -*-
import urllib.request
import random
import datetime


# ユーザ情報を入れると、そのユーザの住所として登録されている地域の気象情報を返す関数
def get_weather(userdata):
    # ユーザ情報から住所成分を抽出
    address = userdata["住所"].split()

    #今日の天気の取得
    today = datetime.date.today()
    weather = random.randint(1,3)
   
    if(weather == 1):
       weather_text = get_temperture()

    elif(weather == 2):
       weather_text = get_state()

    elif(weather == 3):
       weather_text = get_warning()

    return weather_text


def get_temperture():
    
    # ユーザ情報から住所成分を抽出
    userdata = eval(open("../data/user_profile/user_info.txt","r").read())
    address = userdata["住所"].split()

    #日付の取得
    today = datetime.date.today()
    
    #1 気温を理由に休む
    # livedoorのweather hacksのRSSから、在住都道府県の気温をまとめたXMLデータを取得
    url = "http://weather.livedoor.com/forecast/rss/area/" + address[1] + "0010.xml"
    xml_temperture = urllib.request.urlopen(url).read().decode("utf-8").splitlines()

    # XMLデータの各行から、詳しい住所の気温データを検索
    temperture = []
    for line in xml_temperture:
      # 住所の気温が記載されている行を見つけたら、その行から気温部分のテキストのみを切り出す
      if("<title>" in line and str(today.day)+"日" in line):
        temperture = 18
              
        if(temperture >= 25):
           weather_text1 = "気温が"+str(temperture)+"度と高温ですので、\n熱中症予防として"
        elif(temperture <= 0):
           weather_text1 = "気温が"+str(temperture)+"度と低温ですので、\n凍結での転倒防止として"
        elif(temperture < 25 and temperture >0):
           weather_text1 = "気温が"+str(temperture)+"度と普通ですが、\n今日は、温度差が激しい日とTVで言っていたので、\n"
        return weather_text1


def get_state():
    # ユーザ情報から住所成分を抽出
    userdata = eval(open("../data/user_profile/user_info.txt","r").read())
    address = userdata["住所"].split()

    #日付の取得
    today = datetime.date.today()
    #2 天気を理由に休む
    #livedoorのweather hacksのRSSから、在住都道府県の天気をまとめたXMLデータを取得
    url = "http://weather.livedoor.com/forecast/rss/area/" + address[1] + "0010.xml"
    xml_state = urllib.request.urlopen(url).read().decode("utf-8").splitlines()

    # XMLデータの各行から、詳しい住所の天気データを検索
    state = []
    for line in xml_state:
      # 住所の天気が記載されている行を見つけたら、その行から天気部分のテキストのみを切り出す
      if("<title>" in line and "月"+str(today.day)+"日" in line):
        
        state = "yuki"
        #state= line.split()         
        #warning = line.split(" - ")[1].split("が発表されています")[0].split("、")
     

        if(state == "暴風雪" or state == "雨で暴風を伴う" or state == "雨" or state == "雪"):
          weather_text2 = "今日の天気が"+state+"ということで悪天候なので\n"
        elif(state != "暴風雪" or state != "雨で暴風を伴う" or state != "雨" or state != "雪"):
          weather_text2 = "天気は今は大丈夫なのですが、今朝ご飯粒がお茶椀から綺麗にとれました。\nよって、先人の伝えを信じると雨の恐れがあるので、"
          return weather_text2 


def get_warning():
    # ユーザ情報から住所成分を抽出
    userdata = eval(open("../data/user_profile/user_info.txt","r").read())
    address = userdata["住所"].split()

    #日付の取得
    today = datetime.date.today()
    #3 注意報・警報を元に休む
    # livedoorのweather hacksのRSSから、在住都道府県の注意報・警報をまとめたXMLデータを取得
    url = "http://weather.livedoor.com/forecast/rss/warn/" + address[1] + ".xml"
    xml_warning = urllib.request.urlopen(url).read().decode("utf-8").splitlines()

    # XMLデータの各行から、詳しい住所の注意報・警報データを検索 
    warning = []
    for line in xml_warning:
      # 住所の注意報・警報が記載されている行を見つけたら、その行から注意報・警報部分のテキストのみを切り出す
      if("<title>"+address[2] in line and "発表されていません。" not in line):
         warning = line.split(" - ")[1].split("が発表されています")[0].split("、")
         weather_text3 = "現在" + warning + "が発令されていますので、\n"
      elif("<title>"+address[2] in line and "発表されていません。" in line):
         weather_text3 = "注意報も警報も出ていないのですが、嫌な予感がします。\nよって、"
         return weather_text3


if(__name__ == "__main__"):
    # ユーザ情報を読み込む
    userdata = eval(open("../data/user_profile/user_info.txt","r").read())
    # 関数を呼び出す
    print(get_weather(userdata))
