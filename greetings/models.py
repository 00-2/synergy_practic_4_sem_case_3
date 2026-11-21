from django.db import models


class Greeting(models.Model):
    name = models.CharField(max_length=100)
