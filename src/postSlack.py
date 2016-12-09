# -*- coding: utf-8 -*-
from slacker import Slacker
import random
import glob


# Slackの指定されたチャンネルにテキストを投稿する関数
def post_slack(text, channel, token, as_user_flag=True):
    # 自動投稿と明示(テスト用処理、本番では外す)
    text = text + "(このメッセージは自動投稿です)\n" + "-" * 50

    slacker = Slacker(token)
    slacker.chat.post_message(channel, text, as_user=as_user_flag)
    #print(text)


# 投稿テキストのスロットにユーザ情報を挿入する関数
def insert_slot(message, userdata):
    # スロット一覧
    slots = userdata.keys()
    # それぞれのスロットに、対応するユーザ情報の値を挿入する
    for slot in slots:
        if(slot == "住所"):
            message = message.replace("<住所(都道府県)>", userdata[slot].split()[0])
            message = message.replace("<住所(詳細地域)>", userdata[slot].split()[2])
        else:
            message = message.replace("<"+slot+">", userdata[slot])
    # 結果を返す
    return message


# 休みますメッセージを投稿するための関数
def post_RestMessage(text, userdata):
    # templateフォルダから欠勤メッセージのテンプレートを検索・ランダムに選択・読み込み
    templates = list(glob.glob("../data/template/*.txt"))
    template = random.choice(templates)
    message = open(template, "r").read()
    # テンプレートに欠勤テキストを挿入
    message = message.replace("<TEXT>", text)
    # その他スロットにユーザの情報を挿入
    message = insert_slot(message, userdata)
    # slackに投稿
    post_slack(message, userdata["チャンネル"], userdata["トークン"])

def post_BotMessage(bottext,userdata):
    post_slack(bottext, userdata["チャンネル"], userdata["トークン"], as_user_flag=False)

def post_OwnSlack(responsetext,userdata):
    post_slack(responsetext, userdata["ユーザid"], userdata["トークン"], as_user_flag=False) #要確認

if(__name__ == "__main__"):
    ####### 投稿用データ(それぞれ仮の値 本来は他の処理で生成する) #######
    # SlackAPIで発行したtokenID
    token = "xoxp-***********-***********-***********-********************************"
    # 投稿するチャンネル名
    channel = "random"
    # ユーザ情報
    userdata = {"名前": "上野", "所属": "山形大学 井上研究室", "トークン": token, "チャンネル": channel}
    # 投稿する理由テキスト
    text = "風邪を引いたので休みます。"
    ################################################################

    # 投稿
    post_RestMessage(text, userdata)
