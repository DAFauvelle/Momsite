from django.contrib import admin

# Register your models here.
from .models import Article, Family, Reference

admin.site.register(Article)
admin.site.register(Family)
admin.site.register(Reference)