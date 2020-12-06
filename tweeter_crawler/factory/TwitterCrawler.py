import json
from datetime import datetime

from MainPy.settings import PROXY_URL
from OrmMongodbRepository.OrmRepository import OrmRepository
from ThraedsAndQueue.DoWorkTwitter import DoWorkTwitter
from tools.Tools import Tools
from tweeter_crawler.factory.IFactorySocial import IFactorySocial
import time
import tweepy

""" This class is a crawler for get data from twitter by api's twitter """


class TwitterCrawler(IFactorySocial):

    # read tweets from twitter and save it in mongodb database
    @staticmethod
    def read_and_save(request):

        consumer_key = ""
        consumer_secret = ""
        access_token = ""
        access_token_secret = ""

        tweets = []
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth, proxy=PROXY_URL)
        username = request.data.get('username')

        timeline = tweepy.Cursor(api.user_timeline, id=username,tweet_mode='extended').items(20)

        start_date = datetime.fromisoformat(str(request.data.get('start_date')))
        end_date = datetime.fromisoformat(str(request.data.get('end_date')))
        url_video = ""
        # for in timeline twitter user=username
        for tweet in timeline:
            created_at = datetime.fromisoformat(time.strftime('%Y-%m-%d',
                                                              time.strptime(str(tweet.created_at),
                                                                            '%Y-%m-%d %H:%M:%S')))

            for media in tweet.entities.get("media", [{}]):
                if created_at >= start_date and created_at <= end_date:
                    if str(media.get("media_url")) in str(tweet.entities.get("media", [{}])):

                        # get url video from tweets
                        if hasattr(tweet,"extended_entities"):
                            if "video_info" in str(tweet.extended_entities.get("media", [{}])[0]):
                                for link in tweet.extended_entities.get("media", [{}])[0]["video_info"]["variants"]:
                                    if "video" in str(link.get("content_type")):
                                         url_video = link.get("url")

                        json_make_with_media = {
                            "tweet_id": int(tweet.id),
                            "username": username,
                            "type": "Tweet_with_Media",
                            "media": str(media.get("media_url")),
                            "url_video": url_video,
                            "text": str(tweet.full_text),
                            "created_at": str(tweet.created_at)
                           }
                        tweets.append(json_make_with_media)
                        url_video = ""
                        DoWorkTwitter.add_qeueu( json_make_with_media)

                    else:
                        json_make = {
                            "tweet_id": int(tweet.id),
                            "username": username,
                            "type": "Between_Date",
                            "text": tweet.full_text,
                            "media": str(media.get("media_url")),
                            "created_at": str(tweet.created_at)
                        }
                        tweets.append(json_make)
                        DoWorkTwitter.add_qeueu(json_make)

        DoWorkTwitter.len = len(tweets)
        DoWorkTwitter.doing()
        return tweets

    # save images in drive from binary field database
    @staticmethod
    def save_images(request):
        return Tools.save_images(request.data.get('key'), request.data.get('value'))

    # read all documents from mongodb all data
    @staticmethod
    def read_data_from_mongodb():
        return OrmRepository.read_data()

    # find data from database with two param key and value
    @staticmethod
    def find_data(request):
        data = []
        for field in OrmRepository.find(request.data.get('key'), request.data.get('value')):
            json_make = {
                "read": "true",
                "tweet_id": str(field.tweet_id),
                "username": field.username,
                "type ": "Tweet_with_Media",
                "media": field.media,
                "text": field.text,
                "created_at": str(field.created_at),
                "binary_file": str(field.binary_file)
            }
            data.append(json_make)
        return data

"""
 json_str = json.dumps(tweet._json)
            if hasattr(tweet, 'extended_entities'):
                j = json.loads(json_str)
                video_info = j["extended_entities"]["media"]
                for video in video_info:
                    for vid in video["video_info"]["variants"]:

                         print(vid["url"])
"""