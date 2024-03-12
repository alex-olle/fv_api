from django.db import models


# Create your models here.
class Fruit(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False, null=False)
    proximity = models.BooleanField(default=True, blank=False, null=False)
    blocked = models.BooleanField(default=True)

    def __str__(self):
        return self.name
