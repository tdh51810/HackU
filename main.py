import random
import get_warning
import postSlack

# ユーザ情報を読み込む
userdata = eval(open("user_profile/user_info.txt","r").read())

# 理由テキストの生成に成功するまでループする
text = None
while(text is None):
	# 理由生成アルゴリズムをランダムに選択
	algorithm = random.randint(1,2)

	# 注意報・警報データを用いた理由生成
	if(algorithm == 1):
		# 注意報・警報データを取得し、存在するならテキストを生成
		warning = get_warning.get_warning(userdata)
		if(len(warning) > 0):
			text = "私が住んでいる<住所>で"+ "と".join(warning) + "が\n発令されているので、念のため休ませていただきます。"

	# 定型文による理由生成(仮)
	elif(algorithm == 2):
		text = "風邪を引いたので休みます。"

# 整形してSlackに投稿
postSlack.post_RestMessage(text, userdata)
