import random

# 自分の病気を伝えて休む関数
def my_disease(userdata):
	diseases = ["歯痛がひどく歯医者に行きます","ぎっくり腰になってしまった","風邪をひいて","骨折をしてしまった","高熱が出てしまった","蕁麻疹が出てしまった","感染症の疑いがあり病院へ行きます"]
	myreason = random.choice(diseases)
	return myreason

if(__name__ == "__main__"):
	# ユーザ情報を読み込む
	userdata = eval(open("user_profile/user_info.txt","r").read())
	# 関数を呼び出す
	#print(my_disease(userdata))
