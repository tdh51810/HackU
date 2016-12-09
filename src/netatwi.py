import random

def neta():
    tweet = open("../data/reason_from_twitter.txt","r").read()
    tweetlist = tweet.split("\n")  #空要素をリストから削除
    while(True):
        try:
            tweetlist.remove("")
        except ValueError:
            break

    one_tweet = random.choice(tweetlist)
    text = one_tweet
    restext = "送信が完了しました。"
    return [text,restext]
