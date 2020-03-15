from django.db import models
from django.utils import timezone

AA_CHOICES = [('None','None'),
                ('US Large','US Large'),
                ('US Small', 'US Small'),
                ('All country', 'All country'),
                ('EAFE', 'EAFE'),
                ('Emerging Markets', 'Emerging Markets'),
                ('US Treasury Short', 'US Treasury Short'),
                ('US Treasury Long', 'US Treasury Long'),
                ('US Treasury Intermediate', 'US Treasury Intermediate'),
                ('US Corporate Intermediate', 'US Corporate Intermediate'),
                ('US High Yield', 'US Aggregate'),
                ('US Aggregate', 'US Aggregate'),
                ('US Tips', 'US Tips'),
                ('Global Ex-US Treasury', 'Global Ex-US Treasury'),
                ('Global Aggregate', 'Global Aggregate'),
                ('Emerging Market (Non-Local)', 'Emerging Market (Non-Local)'),
                ('Emerging Market (Local)', 'Emerging Market (Local)'),
                ('EM Cash', 'EM Cash'),
                ('Commodities', 'Commodities'),
                ('Bank Loans', 'Bank Loans'),
                ('Global Ex-US Corporates', 'Global Ex-US Corporates'),
                ('REITS', 'REITS'),
                ('United States Cash', 'United States Cash'),
                ('US Commercial Real Estate', 'US Commercial Real Estate'),
                ('Global DM Ex-US Long/Short Equity', 'Global DM Ex-US Long/Short Equity'),
                ('US Long/Short Equity', 'US Long/Short Equity'),
                ('Europe LBO', 'Europe LBO'),
                ('US LBO', 'US LBO')]

class AssetClass(models.Model):
    name = models.CharField(max_length=100)
    expected_return = models.FloatField()
    date_created = models.DateTimeField(default=timezone.now)

    def __self__(self):
        return self.name


class Allocation(models.Model):
    name = models.CharField(max_length=100)
    aa_1 = models.CharField(max_length=100, choices=AA_CHOICES, default="None")
    aa_2 = models.CharField(max_length=100, choices=AA_CHOICES, default="None")
    aa_3 = models.CharField(max_length=100, choices=AA_CHOICES, default="None")
    aa_4 = models.CharField(max_length=100, choices=AA_CHOICES, default="None")
    aa_5 = models.CharField(max_length=100, choices=AA_CHOICES, default="None")
    aa_6 = models.CharField(max_length=100, choices=AA_CHOICES, default="None")
    aa_7 = models.CharField(max_length=100, choices=AA_CHOICES, default="None")
    aa_8 = models.CharField(max_length=100, choices=AA_CHOICES, default="None")
    aa_9 = models.CharField(max_length=100, choices=AA_CHOICES, default="None")
    aa_10 = models.CharField(max_length=100, choices=AA_CHOICES, default="None")

    def __self__(self):
        return self.name


