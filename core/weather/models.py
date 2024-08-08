from django.db import models

class Weather(models.Model):
    lantitude = models.FloatField(max_value=100)
    longtitude = models.FloatField(max_value=100)
    temperature = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)