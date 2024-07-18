from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=300, null=True)
    number_of_searches = models.IntegerField(default=0)

    def __str__(self):
        return self.name
