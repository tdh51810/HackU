# -*- coding: utf-8 -*-
import urllib.request


# ユーザ情報を入れると、そのユーザの住所として登録されている地域に発令されている注意報・警報を返す関数
def get_warning(userdata):
    # ユーザ情報から住所成分を抽出
    address = userdata["住所"].split()
    # livedoorのweather hacksのRSSから、在住都道府県の注意報・警報をまとめたXMLデータを取得
    url = "http://weather.livedoor.com/forecast/rss/warn/" + address[1] + ".xml"
    xml_warning = urllib.request.urlopen(url).read().decode("utf-8").splitlines()

    # XMLデータの各行から、詳しい住所の注意報・警報データを検索
    warning = []
    for line in xml_warning:
        # 住所の注意報・警報が記載されている行を見つけたら、その行から注意報・警報部分のテキストのみを切り出す
        # 注意報・警報が発令されていない場合は無視
        if("<title>"+address[2] in line and "発表されていません。" not in line):
            warning = line.split(" - ")[1].split("が発表されています")[0].split("、")
        # 得られた注意報・警報一覧を返す
        return warning


if(__name__ == "__main__"):
    # ユーザ情報を読み込む
    userdata = eval(open("../data/user_profile/user_info.txt","r").read())
    # 関数を呼び出す
    print(get_warning(userdata))
