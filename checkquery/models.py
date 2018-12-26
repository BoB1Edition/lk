from django.db import models

# Create your models here.
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
