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

from django.db import models


class QueuesConfig(models.Model):
    extension = models.CharField(primary_key=True, max_length=20)
    descr = models.CharField(max_length=35)
    grppre = models.CharField(max_length=100)
    alertinfo = models.CharField(max_length=254)
    ringing = models.IntegerField()
    maxwait = models.CharField(max_length=8)
    password = models.CharField(max_length=20)
    ivr_id = models.CharField(max_length=8)
    dest = models.CharField(max_length=50)
    cwignore = models.IntegerField()
    queuewait = models.IntegerField(blank=True, null=True)
    use_queue_context = models.IntegerField(blank=True, null=True)
    togglehint = models.IntegerField(blank=True, null=True)
    qnoanswer = models.IntegerField(blank=True, null=True)
    callconfirm = models.IntegerField(blank=True, null=True)
    callconfirm_id = models.IntegerField(blank=True, null=True)
    qregex = models.CharField(max_length=255, blank=True, null=True)
    agentannounce_id = models.IntegerField(blank=True, null=True)
    joinannounce_id = models.IntegerField(blank=True, null=True)
    monitor_type = models.CharField(max_length=5, blank=True, null=True)
    monitor_heard = models.IntegerField(blank=True, null=True)
    monitor_spoken = models.IntegerField(blank=True, null=True)
    callback_id = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'queues_config'
