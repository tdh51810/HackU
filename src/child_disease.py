import random

# 子供の病気を伝えて休む関数
def child_disease(userdata):
    if(userdata["子ども"] != "0"):
        diseases = ["を歯医者に連れていきます","が風邪をひいてしまった","が骨折をしてしまった","が熱を出してしまった","に蕁麻疹が出てしまった","感染症の疑いがあり病院へ連れていきます"]
        childreason = random.choice(diseases)
        text = "おはようございます。\n申し訳ないのですが、子供" + childreason + "ので、今日はお休みをいただきます。"
        restext = "ここにレスポンスの文章が入るよ"
        return [text,restext]
    else:
        text = None
        restext = "ここにエラーメッセージの文章が入るよ"
        return [text,restext]
