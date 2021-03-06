from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'lkview'
urlpatterns = [
    url('', views.main, name='main'),
    path('ring/', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
