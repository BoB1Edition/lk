from django.urls import path
from django.conf.urls import url

#from . import views
from django.conf.urls.static import static
from django.conf import settings
from blackaster.views import *

app_name = 'blackaster'
urlpatterns = [
    url(r'^$', BlackAster, name='BlackAster'),
    url(r'^js/main.js$', BlackMainJS, name='BlackMainJS'),
    url(r'^listen/(\d+)', Listen, name='Listen'),
    url(r'test/', test, name='test')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
