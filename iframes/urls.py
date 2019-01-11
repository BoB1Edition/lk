from django.urls import path
from django.conf.urls import url
from django.conf import settings

from django.conf.urls.static import static
from iframes.views import queuestats

urlpatterns = [
    url('queue-stats$', queuestats, name='queue-stats'),
    #path('ring/', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
