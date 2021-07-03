from django.conf.urls import url
from django.conf import settings
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$',views.image,name = 'image'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^detail/(\d+)', views.detail, name='detail'),
    url(r'^location/(\d+)', views.location, name='location'),
    # url(r'^share/(\d+)', views.share, name='share'),
  
]
