from mongoengine import Document, fields

# Create your models here.


class Tweet(Document):
    tweet_id = fields.IntField()
    text = fields.StringField()
    media = fields.StringField()
    binary_file = fields.BinaryField()
    username = fields.StringField()
    type = fields.StringField()
    created_at = fields.DateTimeField(null=False)
