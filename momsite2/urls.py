from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from articles import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'momsite2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^admin/', include(admin.site.urls)),
   # url(r'^homepage/', views.homepage, name = 'homepage'),
    url(r'^$', views.homepage),
    #url(r'^dostie/', views.dostie),
    #url(r'^$', views.bonjour),
    url(r'^articles/', include('articles.urls')),
    #url(r'^brunelle/', views.brunelle),
    url(r'^famille/(?P<famille>.*)/', views.famille, name='family-detail'),
    url(r'^bibliographie/', views.bibliographie, name = 'bibliographie-detail'),
    
    # Echange les urls specifique aux articles
]
