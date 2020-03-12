from django.db import models
from django.utils import timezone

class AssetClass(models.Model):
    name = models.CharField(max_length=100)
    expected_return = models.FloatField()
    date_created = models.DateTimeField(default=timezone.now)

    def __self__(self):
        return self.name


class Allocation(models.Model):
    name = models.CharField(max_length=100)
    aa_1 = models.CharField(max_length=100)
    aa_2 = models.CharField(max_length=100)
    aa_3 = models.CharField(max_length=100)
    aa_4 = models.CharField(max_length=100)

    def __self__(self):
        return self.name

