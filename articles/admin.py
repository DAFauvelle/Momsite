from django.contrib import admin

# Register your models here.
from .models import Article, Family, Reference, Liens, Photos

admin.site.register(Article)
admin.site.register(Family)
admin.site.register(Reference)
admin.site.register(Liens)
admin.site.register(Photos)