
from django.db import models

class ScrapedData(models.Model):
    ip = models.CharField(max_length=50)
    port = models.IntegerField()
    protocol = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    uptime = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.ip}:{self.port}'
