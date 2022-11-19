from django.db import models


# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name} ..."


class Product(models.Model):
    name = models.CharField(max_length=250)
    topic = models.ForeignKey(Topic, default="Book", on_delete=models.SET_DEFAULT)
    file_path = models.CharField(max_length=500)
    subject = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.description[0:20] + "..."


class Consumer(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}  {self.description[0:20]} ..."
