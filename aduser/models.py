from django.db import models
from ldap3 import Server, Connection, ALL
from django.conf import settings
from django.db import models
from django.db.models.base import ModelState
from django.contrib.auth.models import AbstractUser, User, AbstractBaseUser, Group
import datetime


class aduser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True, default=None)
    sid = models.CharField(max_length=46, null=True)
    telephoneNumber = models.CharField(max_length=20, null=True)
    # username =  models.TextField(null=False)
    # password =  models.TextField(null=False)

    template_filter = '(userPrincipalName=%s)'
    connection = None
    groups = models.ManyToManyField('adgroups')

    def fill(self, user):
        domain = settings.JSON_SETTINGS['domain']
        s = Server(domain, get_info=ALL)
        c = Connection(s, user=('%s@%s' % (user.username, domain)),
        password=user.password)
        if c.bind():
            filter = self.template_filter % ('%s@%s' % (user.username, domain))
            c.search(settings.JSON_SETTINGS['BaseDN'], filter, attributes=['*'])

            self.user = user
            self.user.is_staff = 1

            self.sid = c.entries[0]['objectSid'].value
            self.user.save()
            grs = c.entries[0]['memberOf']
            gr = [x.split(',')[0][3:] for x in grs.values]
            self.telephoneNumber = c.entries[0]['telephoneNumber'].value
            self.save()
            for g in gr:
                if g == 'PBX-admin':
                    self.user.is_superuser = 1
                NewGroup, _ =Group.objects.get_or_create(name=g)
                NewGroup.save()
                group, gcreated = adgroups.objects.get_or_create(groupname=g,
                group = NewGroup)
                group.save()
                self.groups.add(group)
                self.user.groups.add(NewGroup)
                group.user.add(self)
            self.save()
        else:
            self.user = None
        return self.user


class adgroups(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE, default=None)
    user = models.ManyToManyField('aduser')
    groupname = models.TextField(null=True)
    #id = models.AutoField(primary_key=True, default=1)
