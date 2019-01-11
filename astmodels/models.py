from django.db import models

# Create your models here.
from django.db import models


class Users(models.Model):
    extension = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    voicemail = models.CharField(max_length=50, blank=True, null=True)
    ringtimer = models.IntegerField(blank=True, null=True)
    noanswer = models.CharField(max_length=100, blank=True, null=True)
    recording = models.CharField(max_length=50, blank=True, null=True)
    outboundcid = models.CharField(max_length=50, blank=True, null=True)
    sipname = models.CharField(max_length=50, blank=True, null=True)
    noanswer_cid = models.CharField(max_length=20)
    busy_cid = models.CharField(max_length=20)
    chanunavail_cid = models.CharField(max_length=20)
    noanswer_dest = models.CharField(max_length=255)
    busy_dest = models.CharField(max_length=255)
    chanunavail_dest = models.CharField(max_length=255)
    mohclass = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
