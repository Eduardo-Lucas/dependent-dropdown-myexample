from django.db import models
from django.urls import reverse


class BusinessLine(models.Model):
    description = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.description


class ProfitCenter(models.Model):
    businessline = models.ForeignKey(BusinessLine, default=1, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, default='New Profit Center',)

    class Meta:
        ordering = ['businessline', 'description']
        unique_together = ['businessline', 'description']

    def __str__(self):
        return self.description


class Project(models.Model):
    description = models.CharField(max_length=50, unique=True)
    businessline = models.ForeignKey(BusinessLine, on_delete=models.CASCADE)
    profitcenter = models.ForeignKey(ProfitCenter, on_delete=models.CASCADE)

    class Meta:
        ordering = ['businessline', 'profitcenter', 'description']
        unique_together = ['businessline', 'profitcenter', 'description']

    def __str__(self):
        return self.description
