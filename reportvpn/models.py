from django.db import models

# Create your models here.
class Connections(models.Model):
    cisco = models.CharField(max_length=50, blank=True, null=True)
    ciscotag = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    user = models.CharField(max_length=45, blank=True, null=True)
    field_version = models.IntegerField(db_column='@version', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    type = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    host = models.CharField(max_length=20, blank=True, null=True)
    ip = models.CharField(max_length=20, blank=True, null=True)
    field_timestamp = models.DateTimeField(db_column='@timestamp', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    syslog_pri = models.CharField(max_length=10, blank=True, null=True)
    group = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'connections'
