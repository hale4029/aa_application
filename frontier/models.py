from django.db import models
from django.utils import timezone

class AssetClass(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)

    def __self__(self):
        return self.name