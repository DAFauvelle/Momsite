from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from articles import views

urlpatterns = [

#List of URLs relevant to the app
    #url(r'^articles/', include('articles.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^articles/', include('articles.urls')),
    url(r'^famille/(?P<famille>.*)/', views.famille, name='family-detail'),
    url(r'^bibliographie/', views.bibliographie, name = 'bibliographie-detail'),
    url(r'^liens/',views.liens, name = 'liens-detail'),
    url(r'^ckeditor/', include('ckeditor.urls')),
    # Echange les urls specifique aux articles
]

#Code to indicate where to look for media
media_pattern = r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/')

if settings.DEBUG:
    urlpatterns += patterns(  # NOQA
        '',
        url(media_pattern, 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    )