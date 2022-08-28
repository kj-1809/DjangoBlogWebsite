from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    info = models.CharField(max_length = 40 , default = "")
    content = models.CharField(max_length=10000000)
    image = models.ImageField(default = "", null = True , upload_to = "images/")
    featured = models.BooleanField(default = False)

    def __str__(self):
        return self.title + " " + str(self.id)
        


