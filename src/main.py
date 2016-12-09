# -*- coding: utf-8 -*-
import random
import time
import get_warning
import postSlack
import file_func
import get_weather
import my_disease
import child_disease
import sinseki
import netatwi


while True:
    while True:
        trigger = file_func.get_triger
        if trigger != False:
            # プロフィールの更新を確認
            file_func.get_prof()
            break

    # ユーザ情報を読み込む
    userdata = eval(open("../data/user_profile/user_info.txt","r").read())
    text = None

    # 緊急ボタン(赤：休み)
    if(trigger == "red"):
        text,restext = "一身上の都合により休ませていただきます。","正常に送信されました。"  #bttnはエラー文生成無し
        bottext = "了解です！お大事に！"

    # 緊急ボタン(青：遅刻)
    if(trigger == "blue"):
        text,restext = "寝坊してしまい、遅刻します。急いで向かいます。","正常に送信されました。"  #bttnはエラー文生成無し
        bottext = "了解しました。気をつけてね。"


    # 天気を理由にして休む場合
    if(trigger == "weather"):
        # 注意報・警報データを取得し、存在するならテキストを生成
        text,restext = get_weather.get_weather(userdata)   # slackのチャンネルに送られるテキスト,ユーザへのレスポンステキスト
        bottext = ""                                       # botが肯定するためのテキスト

    # 自分が風邪を引いて休む場合
    elif(trigger == "own_cold"):
        #text,restext = my_disease.mydisease(userdata)
        bottext = ""

    # 子どもが風邪を引いて休む場合
    elif(trigger == "child_cold"):
        #text,restext = child_disease.child_disease(userdata)
        bottext = ""

    # 親戚の不幸で休む場合
    elif(trigger == "relative"):
        #text,restext = sinseki.kill()
        bottext = ""

    # ネタツイートを引用する場合
    elif(trigger == "twitter"):
        #text,restext = netatwi.neta()
        bottext = ""

    # 理由生成に失敗した場合
    if(text == None):
        postSlack.post_OwnSlack(restext,userdata)

    # 理由生成に成功した場合
    else:
        # 整形してSlackに投稿
        postSlack.post_RestMessage(text, userdata)

        # Botが休み・遅刻を肯定するようなメッセージを投稿
        time.sleep(5)
        postSlack.post_BotMessage(bottext, userdata)

        #ユーザのslackにレスポンスを送信
        postSlack.post_OwnSlack(restext,userdata)
