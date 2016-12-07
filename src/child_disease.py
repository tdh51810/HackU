import random

# 子供の病気を伝えて休む関数
def child_disease(userdata):
	diseases = ["を歯医者に連れていきます","が風邪をひいてしまった","が骨折をしてしまった","が熱を出してしまった","に蕁麻疹が出てしまった","感染症の疑いがあり病院へ連れていきます"]
	childreason = random.choice(diseases)
	return childreason

if(__name__ == "__main__"):
	# ユーザ情報を読み込む
	userdata = eval(open("user_profile/user_info.txt","r").read())
	# 関数を呼び出す
	#print(child_disease(userdata))
