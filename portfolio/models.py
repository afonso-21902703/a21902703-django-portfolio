from django.db import models


class Programmer(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50,
                                null=True,
                                blank=True)
    photo = models.ImageField(upload_to='portfolio/',
                              null=True,
                              blank=True)

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
    utubeLink = models.CharField(max_length=100,
                                 null=True,
                                 blank=True)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Technologies(models.Model):
    name = models.CharField(max_length=50)
    acronym = models.CharField(max_length=10)
    birth = models.DateField(auto_now=False)
    creator = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='portfolio/',
                             blank=False)
    site = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    useDesc = models.CharField(max_length=500,
                               null=True,
                               blank=True)
    usedInWeb = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    image = models.ImageField(upload_to='portfolio/',
                              blank=False)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Lab(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Patterns(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=500,
                            null=True,
                            blank=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               related_name='posts')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    link = models.CharField(max_length=500,
                            null=True,
                            blank=True)
    image = models.ImageField(upload_to='portfolio/',
                              blank=False)

    def __str__(self):
        return self.title


class SocialMedia(models.Model):
    title = models.CharField(max_length=20)
    link = models.CharField(max_length=500)
    image = models.ImageField(upload_to='portfolio/',
                              blank=False)

    def __str__(self):
        return self.title
