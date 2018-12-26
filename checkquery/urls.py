from django.conf.urls import url
from django.urls import path
from checkquery.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url('^$', checkqueryMain, name='checkqueryMain'),
    url('^js/main.js$', MainJS, name='MainJS'),
    url('^queue/([0-9]{4})', queue, name='queue'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
