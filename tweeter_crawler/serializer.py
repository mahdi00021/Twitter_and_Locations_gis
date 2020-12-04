from rest_framework import serializers

from tweeter_crawler.models import Tweet


""" This class for handle complex data to json for parsing"""


class TweetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['text', 'media', 'username', 'type', 'created_at']
