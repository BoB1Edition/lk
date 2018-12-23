"""lk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include
from lkview import views as lk
from aduser import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^record/number/([0-9]+)/', lk.number, name='number'),
    url(r'^$', lk.main, name='main'),
    url(r'^convert/(.*)$', lk.convert, name='convert'),
    url(r'^js/main.js$', lk.mainjs, name='main.js'),
    url(r'^ring/', lk.index, name='index'),
    url(r'^search/', include('search.urls')),
    #url(r'^accounts/login/$', include('django.contrib.auth.views.LoginView'),
    #{'template_name': 'registration/login.html', 'authentication_form': views.LoginForm}),
    url(r'^accounts/login/$', LoginView.as_view(template_name='registration/login.html',
    authentication_form=views.LoginForm), name="login"),
    url(r'^accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
