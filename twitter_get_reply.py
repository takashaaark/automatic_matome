import tweepy
import time
from datetime import datetime
from twitter_settings import *

MAX_WAIT = 30


def get_reply():
    """
    ツイッターのリプを受け取り、4桁の数字列を返す
    :return:
    """

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    # print("API完了")

    start_time = int(datetime.utcnow().strftime("%Y%m%d%H%M%S"))
    print(start_time)

    print("返事を待ちます...最大" + str(MAX_WAIT) + '分')

    count = 0
    number = None
    while count < int(MAX_WAIT):
        timeline = api.mentions_timeline()
        status = timeline[0]
        reply_time = int(status.created_at.strftime("%Y%m%d%H%M%S"))
        if reply_time > start_time:
            number = status.text[9:13]
            print("来ました!", reply_time)
            print(number)
            # 返信する場合
            status_id = status.id
            screen_name = status.author.screen_name
            reply_text = "@" + screen_name + " " + "助かります: " + str(reply_time)
            api.update_status(status=reply_text, in_reply_to_status_id=status_id)
            break

        time.sleep(60)
        count += 1
    return number
