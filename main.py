"""
NAVERまとめにログインして記事を投稿する。
画像認証がある
"""

import tabelog_search
import matome_publish
import title_maker

import twitter_tweet


if __name__ == "__main__":

    twitter_tweet.tweet_sentence("仕事を始めるか")

    Tabe = tabelog_search.TabelogSearch()

    pref_name = Tabe.pref_name
    target_name = Tabe.target_name

    title = title_maker.title_maker(pref_name, target_name)
    twitter_tweet.tweet_sentence("タイトルは\"" + title + "\"に決めたぞ")

    img_file = Tabe.image_file
    data_list = Tabe.rank_list

    Matome = matome_publish.MatomePublish(title, img_file, data_list)

    twitter_tweet.tweet_sentence("完成だ。")


