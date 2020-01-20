from django.db import models

# Create your models here.
class Dataset(models.Model):

    date = models.fields.DateField()
    channel = models.fields.CharField(max_length=20)
    country = models.fields.CharField(max_length=2)
    os = models.fields.CharField(max_length=7)
    impressions = models.fields.IntegerField()
    clicks = models.fields.IntegerField()
    installs = models.fields.IntegerField()
    spend = models.fields.FloatField()
    revenue = models.fields.FloatField()

