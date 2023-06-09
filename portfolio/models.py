from django.db import models


class Programmer(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Project(models.Model):

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/',
                              null=True,
                              blank=True)
    cadeira = models.CharField(max_length=100)
    programmers = models.ManyToManyField(Programmer)
    gitLink = models.CharField(max_length=100)
    tecnologies = models.CharField(max_length=100)
    utubeLink = models.CharField(max_length=100, null=True,blank=True)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title

