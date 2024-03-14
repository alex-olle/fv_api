from django.db import models
from fruits.models import Fruit
from vegetables.models import Vegetable


# Create your models here.
class Month(models.Model):
    name = models.CharField(max_length=20)
    slug = models.CharField(max_length=20)
    number = models.IntegerField()
    fruits= models.ManyToManyField(Fruit, related_name="fruits", blank=True)
    vegetables = models.ManyToManyField(Vegetable, related_name="vegetables", blank=True)

    class Meta:
        ordering = ["number"]

    def __str__(self):
        return self.name
