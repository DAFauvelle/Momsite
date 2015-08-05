from django.db import models


class Family(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length= 100)
    text = models.TextField()
    family = models.ForeignKey(Family) 
    family_name = family.name
    parent = models.ForeignKey('self')
    #parent_ID = models.IntegerField()
    #article_picture = models.URLField()
    
    
    def __unicode__(self):
        return self.title
        
class Reference(models.Model):
    title = models.CharField(max_length=255)
    article = models.ForeignKey(Article)
    
    def __unicode__(self):
        return self.title