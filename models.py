from django.db import models

# Create your models here.

class Categories(models.Model):
    category = models.CharField(max_length=200)
    description = models.TextField()


    def __str__(self):
        return self.category

class Download(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    artist = models.CharField(max_length=100)
    image = models.ImageField(upload_to='download')

    
    def __str__(self):
        return str(self.category)

class About(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    aimage = models.ImageField(upload_to='about')

    def __str__(self):
        return self.name