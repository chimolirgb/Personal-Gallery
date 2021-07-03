from django.conf.urls import url
from django.conf import settings
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
  
]