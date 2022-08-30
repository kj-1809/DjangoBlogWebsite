from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=70)
    author = models.CharField(max_length=30)
    info = models.TextField(max_length = 150 , default = "")
    content = RichTextField(blank = True , null = True)
    # content = models.CharField(max_length=10000000)
    image = models.ImageField(default = "", null = True , upload_to = "images/")
    featured = models.BooleanField(default = False)

    def __str__(self):
        return self.title + " " + str(self.id)
        


