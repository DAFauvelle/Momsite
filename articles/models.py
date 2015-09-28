from django.db import models
from ckeditor.fields import RichTextField

class Family(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length= 100)
    text = RichTextField()
    family = models.ForeignKey(Family)
    family_name = family.name
    #parent = models.ForeignKey('self')

    def __unicode__(self):
        return self.title

class Reference(models.Model):
    title = models.CharField(max_length=255)
    article = models.ForeignKey(Article)

    def __unicode__(self):
        return self.title

class Liens(models.Model):
    title = models.CharField(max_length=255)
    addresse = models.URLField(max_length=255)

    def __unicode__(self):
        return self.title

class Photos(models.Model):
    title = models.CharField(max_length=255)
    la_photo = models.ImageField(upload_to = "images/", max_length = 255)
    article = models.ForeignKey(Article)

    def __unicode__(self):
        return self.title

class ImagePDF(models.Model):
    title = models.CharField(max_length=255)
    la_photo = models.FileField(upload_to = "images/", max_length = 255)
    article = models.ForeignKey(Article)

    def __unicode__(self):
        return self.title
