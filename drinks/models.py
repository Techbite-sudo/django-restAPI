from django.db import models

# Create your models here.

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)


    def __str__(self) -> str:
        return self.name + " " + self.description
    