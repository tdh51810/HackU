# -*- coding: utf-8 -*-
import random
import get_warning
import postSlack
import file_func

while True:
    while True:
        if file_func.get_trig() == True:
            # トリガーを取得
            trigger = file_func.get_trig()
            file_func.get_prof()
            break

    # ユーザ情報を読み込む
    userdata = eval(open("../data/user_profile/user_info.txt","r").read())
    
    text = ""

    # 緊急ボタン(赤：休み)
    if(trigger == "red"):
        text,restext = "一身上の都合により休ませていただきます。"
        bottext = "了解です！お大事に！"

    # 緊急ボタン(青：遅刻)
    if(trigger == "blue"):
        text,restext = "寝坊してしまい、遅刻します。急いで向かいます。",""
        bottext = "了解しました。気をつけてね。"


    # 天気を理由にして休む場合
    if(trigger == "weather"):
        # 注意報・警報データを取得し、存在するならテキストを生成
        text,restext = get_warning.get_warning(userdata)   # slackのチャンネルに送られるテキスト,ユーザへのレスポンステキスト
        bottext = ""                                       # botが肯定するためのテキスト

    # 自分が風邪を引いて休む場合
    elif(trigger == "own_cold"):
        #text,restext = "風邪を引いたので休みます。"
        bottext = ""

    # 子どもが風邪を引いて休む場合
    elif(trigger == "child_cold"):
        #text,restext = "風邪を引いたので休みます。"
        bottext = ""

    # 親戚の不幸で休む場合
    elif(trigger == "relative"):
        #text,restext = "風邪を引いたので休みます。"
        bottext = ""

    # 自分が風邪を引いてしまった場合
    elif(trigger == "twitter"):
        #text,restext = "風邪を引いたので休みます。"
        bottext = ""


    # 理由生成に失敗した場合
    if(text == ""):
        postSlack.post_OwnSlack(restext,userdata)

    # 理由生成に成功した場合
    else:
        # 整形してSlackに投稿
        postSlack.post_RestMessage(text, userdata)

        # Botが休み・遅刻を肯定するようなメッセージを投稿
        postSlack.post_BotMessage(bottext, userdata)

        #ユーザのslackにレスポンスを送信
        postSlack.post_OwnSlack(restext,userdata)
