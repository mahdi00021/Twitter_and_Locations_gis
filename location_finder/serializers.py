from rest_framework import serializers

from location_finder.models import LocationM


class LocationMSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationM
        fields = ['latitude', 'longitude', 'name_point', 'the_geom', 'created_at', 'modified_at']
