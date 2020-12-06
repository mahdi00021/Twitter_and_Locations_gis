from tools.Tools import Tools
from tweeter_crawler.models import Tweet

"""This class for manage data of mongodb"""


class OrmRepository:

    # insert data to mongodb with attributes of data
    # save data not return any
    @staticmethod
    def insert(data):
        if not Tweet.objects(tweet_id=int(data['tweet_id'])):
            Tweet(tweet_id=int(data['tweet_id']), username=data['username'], type=data['type'],
                  media=data['media'], binary_file=Tools.download_file(data['media']),
                  text=str(data['text']), created_at=str(data['created_at'])).save()
            return True
            #print("-------------inserted-----------")
    # read data from mongodb
    # return list of json data
    @staticmethod
    def read_data():

        readt = []

        for field in Tweet.objects():
            jsonmake = {
                "read": "true",
                "tweet_id": str(field.tweet_id),
                "username": field.username,
                "type": field.type,
                "media": field.media,
                "text": field.text,
                "binary": str(field.binary_file),
                "created_at": str(field.created_at),
            }
            readt.append(jsonmake)

        return readt

    # find data with use of key and value
    # return objects
    @staticmethod
    def find(key, value):
        return Tweet.objects(**{key: value})
