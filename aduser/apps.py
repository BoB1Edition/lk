from django.apps import AppConfig
from ldap3 import Server, Connection, ALL
from django.conf import settings
from django.contrib.auth.models import User
from .models import aduser


class AduserConfig(AppConfig):
    name = 'aduser'


class Adauth:
    user = None
    def authenticate(self, request, username=None, password=None):
        print("Adauth: %s, %s " % (username, password))
        domain = settings.JSON_SETTINGS['domain']
        s = Server(domain, get_info=ALL)
        c = Connection(s, user=('%s@%s' % (username, domain)),
        password=password)
        if c.bind():
            u, created = User.objects.get_or_create(username=username)
            u.password=password
            u.save()
            #if created:
            ad, _ = aduser.objects.get_or_create(user=u)
            ad.fill(u)
            self.user = ad
            self.user.save()
            #ad.fill(u)
            u.save()
            return u
        else:
            return None

    def get_user(self, user_id):
        self.user = User.objects.get(pk=user_id)
        return self.user
