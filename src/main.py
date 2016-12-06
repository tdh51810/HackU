# -*- coding: utf-8 -*-
import random
import get_warning
import postSlack
import file_func

while True:
    while True:
        if file_func.get_trig() = True:
            file_func.get_prof()
            break

    # ユーザ情報を読み込む
    userdata = eval(open("../data/user_profile/user_info.txt","r").read())
    
    # 理由テキストの生成に成功するまでループする
    text = None
    while(text is None):
        # 理由生成アルゴリズムをランダムに選択
        algorithm = random.randint(1, 2)
        # 注意報・警報データを用いた理由生成
        if(algorithm == 1):
            # 注意報・警報データを取得し、存在するならテキストを生成
            text = get_warning.get_warning(userdata)
    
        # 定型文による理由生成(仮)
        elif(algorithm == 2):
            text = "風邪を引いたので休みます。"
    
    # 整形してSlackに投稿
    postSlack.post_RestMessage(text, userdata)
    
    # Botが休み・遅刻を肯定するようなメッセージを投稿
    postSlack.post_BotMessage(rest_flag, userdata) # rest_flagはbttnが押された時に生成されるファイルの中身（青（遅刻）:0休み：それ以外）
