import random

# 自分の病気を伝えて休む関数
def my_disease(userdata):
    diseases = ["歯痛がひどく歯医者に行きます","ぎっくり腰になってしまった","風邪をひいてしまった","骨折をしてしまった","高熱が出てしまった","蕁麻疹が出てしまった","感染症の疑いがあり病院へ行きます"]
    myreason = random.choice(diseases)
    text = "おはようございます。\n申し訳ないのですが、" + myreason + "ので、今日はお休みをいただきます。"
    restext = "送信が完了しました。"
    return [text,restext]


