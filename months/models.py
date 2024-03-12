from django.db import models


# Create your models here.
class Month(models.Model):
    name = models.CharField(max_length=20)
    slug = models.CharField(max_length=20)
    number = models.IntegerField()

    class Meta:
        ordering = ["number"]

    def __str__(self):
        return self.name
