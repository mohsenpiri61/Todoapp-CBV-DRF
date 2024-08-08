from django.db import models

class Weather(models.Model):
    lantitude = models.FloatField(null=True)
    longtitude = models.FloatField(null=True)
    temperature = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)