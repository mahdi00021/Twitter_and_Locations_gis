from django.contrib.gis.db import models
# Create your models here.


class LocationM(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    name_point = models.CharField(max_length=100)
    the_geom = models.PointField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
