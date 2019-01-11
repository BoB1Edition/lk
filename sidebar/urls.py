from django.conf.urls import url
from django.urls import path
from sidebar.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^extension/$', extension, name='extension'),
    url(r'^groups/$', groups, name='groups'),
    #path('autocomplete/', autocomplete, name='autocomplete'),
    #path('number/<int:num>', result, name='result'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
