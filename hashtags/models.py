from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=200)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
