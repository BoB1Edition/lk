from django.conf.urls import url
from django.urls import path
from search.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url('^$', searchMain, name='searchMain'),
    url('js/autoFill.js', autoFill, name='autoFill'),
    path('autocomplete/', autocomplete, name='autocomplete'),
    path('number/<int:num>', result, name='result'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
