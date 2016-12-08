# -*- coding: utf-8 -*-
import urllib.request
import random
import datetime
import re

# ユーザ情報を入れると、そのユーザの住所として登録されている地域の気象情報を返す関数
def get_weather(userdata):
    # ユーザ情報から住所成分を抽出
    address = userdata["住所"].split()

    #今日の天気の取得
    today = datetime.date.today()
    
    #どの気象状況を理由に選択するか
    weather = random.randint(1,3)
   
    if(weather == 1):
       weather_text = get_temperture()

    elif(weather == 2):
       weather_text = get_state()

    elif(weather == 3):
       weather_text = get_warning()


    #気象状況を理由に休めたとき
    if(weather_text != 0):
        text = "おはようございます。\n私が住んでいる"+str(address[0])+"で、"+weather_text+"念のため今日は休ませていただきます。"
        restext = "送信が完了しました。"
        return [text,restext]

    #気象状況を理由に休めなかったとき
    elif(weather_text == 0):
        text = "None"    
        restext = "今日は気象状況に問題がないので休めません。"
        return [text,restext]


def get_temperture():
    
    # ユーザ情報から住所成分を抽出
    userdata = eval(open("../data/user_profile/user_prof.txt","r").read())
    address = userdata["住所"].split()

    #日付の取得
    today = datetime.date.today()
    
    #1 気温を理由に休む
    # livedoorのweather hacksのRSSから、在住都道府県の気温をまとめたXMLデータを取得
    if(address[1] == "01a"):
        area_id = "011000"
    elif(address[1] == "01b"):
        area_id = "016010"
    elif(address[1] == "01c"):
        area_id = "013010"
    elif(address[1] == "01d"):
        area_id = "015010"
    else:
        area_id = address[1] + "0010"
    url = "http://weather.livedoor.com/forecast/rss/area/" + area_id + ".xml"
    xml_temperture = urllib.request.urlopen(url).read().decode("utf-8").splitlines()

    # XMLデータの各行から、詳しい住所の気温データを検索
    temperture = []
    for line in xml_temperture:
      # 住所の気温が記載されている行を見つけたら、その行から気温部分のテキストのみを切り出す
      if("<description>" in line and str(today.day)+"日" in line and "℃" in line):

         line = "<description>08日（木）の天気は曇時々雪、最高気温は-4℃ でしょう。</description>"

         if("-" in line):      
            temperture = re.sub("<description>[0-3][0-9]",'',line)     
            temperture = re.sub("[^-\d{1}]?",'',temperture)
        
         elif("-" not in line):
            temperture = re.sub("<description>[0-3][0-9]",'',line)     
            temperture = re.sub("[^-\d{1}]?",'',temperture)
             
         if(int(temperture) >= 30):
            weather_text1 = "気温が"+temperture+"度と高温ですので、\n熱中症予防として"
            return weather_text1

         elif(int(temperture) <= 0):
            weather_text1 = "気温が"+temperture+"度と低温ですので、\n凍結での転倒防止として"
            return weather_text1

         elif(int(temperture) < 30 and int(temperture) >0):
            weather_text1 = 0
            return weather_text1


def get_state():
    # ユーザ情報から住所成分を抽出
    userdata = eval(open("../data/user_profile/user_prof.txt","r").read())
    address = userdata["住所"].split()

    #日付の取得
    today = datetime.date.today()
    #2 天気を理由に休む
    #livedoorのweather hacksのRSSから、在住都道府県の天気をまとめたXMLデータを取得
    if(address[1] == "01a"):
        area_id = "011000"
    elif(address[1] == "01b"):
        area_id = "016010"
    elif(address[1] == "01c"):
        area_id = "013010"
    elif(address[1] == "01d"):
        area_id = "015010"
    else:
        area_id = address[1] + "0010"
    url = "http://weather.livedoor.com/forecast/rss/area/" + area_id + ".xml"
    xml_state = urllib.request.urlopen(url).read().decode("utf-8").splitlines()

    # XMLデータの各行から、詳しい住所の天気データを検索
    state = []
    for line in xml_state:
      # 住所の天気が記載されている行を見つけたら、その行から天気部分のテキストのみを切り出す
      if("<description>" in line and str(today.day)+"日" in line and "℃" in line):
        state = re.sub("<description>[0-3][0-9]日（[^\d{1}]）の天気は",'',line)
        state = re.sub("[\d{2}]",'',state)
        state = re.sub("、[^0-9]*",'',state)
      
        if(state == "暴風雪" or state == "雨で暴風を伴う" or state == "雨" or state == "雪"):
          weather_text2 = "今日の天気が"+state+"ということで悪天候なので\n"
          return weather_text2 
        
        else:
          weather_text2 = 0
          return weather_text2 



def get_warning():
   
    # ユーザ情報から住所成分を抽出
    userdata = eval(open("../data/user_profile/user_prof.txt","r").read())
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
         weather_text3 = "現在" + "と".join(warning) + "が発令されていますので、\n"
         return weather_text3

      elif("<title>"+address[2] in line and "発表されていません。" in line):
         weather_text3 = 0
         return weather_text3 
      


if(__name__ == "__main__"):
    # ユーザ情報を読み込む
    userdata = eval(open("../data/user_profile/user_prof.txt","r").read())
    # 関数を呼び出す
    print(get_weather(userdata))
