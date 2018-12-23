from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cdr(models.Model):
    calldate = models.DateTimeField(primary_key=True)
    clid = models.CharField(max_length=80)
    src = models.CharField(max_length=80)
    dst = models.CharField(max_length=80)
    dcontext = models.CharField(max_length=80)
    channel = models.CharField(max_length=80)
    dstchannel = models.CharField(max_length=80)
    lastapp = models.CharField(max_length=80)
    lastdata = models.CharField(max_length=80)
    duration = models.IntegerField()
    billsec = models.IntegerField()
    disposition = models.CharField(max_length=45)
    amaflags = models.IntegerField()
    accountcode = models.CharField(max_length=20)
    uniqueid = models.CharField(max_length=32)
    userfield = models.CharField(max_length=255)
    did = models.CharField(max_length=50)
    recordingfile = models.CharField(max_length=255)
    cnum = models.CharField(max_length=80)
    cnam = models.CharField(max_length=80)
    outbound_cnum = models.CharField(max_length=80)
    outbound_cnam = models.CharField(max_length=80)
    dst_cnam = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'cdr'

class Astdb(models.Model):
    key = models.CharField(unique=True, max_length=255, blank=True, primary_key=True)
    value = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'astdb'
