from django.urls import path
from django.conf.urls import url

from . import views
from django.conf.urls.static import static
from django.conf import settings
from reportvpn.views import *

# app_name = 'reportvpn'
urlpatterns = [
    url(r'^$', views.reportvpnMain, name='reportvpnMain'),
    url(r'^js/main.js$', views.reportvpnMainJS, name='reportvpnMainJS'),
    url(r'^result$', views.reportvpnMainJS, name='reportvpnMainJS'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
