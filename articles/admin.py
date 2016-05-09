from django.contrib import admin

# Register your models here.
#from django.contrib.admin import ModelAdmin, StackedInline, TabularInline
#from adminsortable2.admin import SortableAdminMixin
from .models import Article, Family, Reference, Liens, Photos, ImagePDF
from . import models


#class MyModelAdmin(SortableAdminMixin, admin.ModelAdmin):
#    model = models.Article


#admin.ModelAdmin
admin.site.register(Article)
admin.site.register(Family)
admin.site.register(Reference)
admin.site.register(Liens)
admin.site.register(Photos)
admin.site.register(ImagePDF)
#admin.StackedInline
#admin.TabularInline


