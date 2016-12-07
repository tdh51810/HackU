# -*- coding: utf-8 -*-
import random
import get_weather
#import postSlack
import my_disease
import child_disease
import urllib.request


#while True:
   #while True:
       #if file_func.get_trig() = True:
           #file_func.get_prof()
           #break

   # ユーザ情報を読み込む
userdata = eval(open("../data/user_profile/user_info.txt","r").read())
   # ユーザ情報から住所成分を抽出
address = userdata["住所"].split()


   # 理由テキストの生成に成功するまでループする
text = None
while(text is None):
      # 理由生成アルゴリズムをランダムに選択
      algorithm = random.randint(1,3)
    
      # 気象データを用いた理由生成
      if(algorithm == 1):
         weather = get_weather.get_weather(userdata)
         text = "おはようございます。\n私が住んでいる"+str(address[0])+"で、"+str(weather)+"念のため今日は休ませていただきます。"
         print(text)
 

      # 自分の病気で休む理由生成
      elif(algorithm == 2):
         mydisease = my_disease.my_disease(userdata)
         text = "おはようございます。\n申し訳ないのですが、" + mydisease + "ので、今日はお休みをいただきます。"
         print(text)
    
      # 子供の病気で休む理由生成
      elif(algorithm == 3):
         childdisease = child_disease.child_disease(userdata)
         text = "おはようございます。\n申し訳ないのですが、子供" + childdisease + "ので、今日はお休みをいただきます。"
         print(text)

 
          
   # 整形してSlackに投稿
   #postSlack.post_RestMessage(text, userdata)

   # Botが休み・遅刻を肯定するようなメッセージを投稿
   #postSlack.post_BotMessage(rest_flag, userdata)
   # rest_flagはbttnが押された時に生成されるファイルの中身（青（遅刻）:0休み：それ以外）
