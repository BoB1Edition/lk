# Generated by Django 2.1.4 on 2018-12-27 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cdr',
            fields=[
                ('calldate', models.DateTimeField(primary_key=True, serialize=False)),
                ('clid', models.CharField(max_length=80)),
                ('src', models.CharField(max_length=80)),
                ('dst', models.CharField(max_length=80)),
                ('dcontext', models.CharField(max_length=80)),
                ('channel', models.CharField(max_length=80)),
                ('dstchannel', models.CharField(max_length=80)),
                ('lastapp', models.CharField(max_length=80)),
                ('lastdata', models.CharField(max_length=80)),
                ('duration', models.IntegerField()),
                ('billsec', models.IntegerField()),
                ('disposition', models.CharField(max_length=45)),
                ('amaflags', models.IntegerField()),
                ('accountcode', models.CharField(max_length=20)),
                ('uniqueid', models.CharField(max_length=32)),
                ('userfield', models.CharField(max_length=255)),
                ('did', models.CharField(max_length=50)),
                ('recordingfile', models.CharField(max_length=255)),
                ('cnum', models.CharField(max_length=80)),
                ('cnam', models.CharField(max_length=80)),
                ('outbound_cnum', models.CharField(max_length=80)),
                ('outbound_cnam', models.CharField(max_length=80)),
                ('dst_cnam', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'cdr',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cel',
            fields=[
                ('eventtype', models.CharField(max_length=30)),
                ('eventtime', models.DateTimeField(primary_key=True, serialize=False)),
                ('cid_name', models.CharField(max_length=80)),
                ('cid_num', models.CharField(max_length=80)),
                ('cid_ani', models.CharField(max_length=80)),
                ('cid_rdnis', models.CharField(max_length=80)),
                ('cid_dnid', models.CharField(max_length=80)),
                ('exten', models.CharField(max_length=80)),
                ('context', models.CharField(max_length=80)),
                ('channame', models.CharField(max_length=80)),
                ('appname', models.CharField(max_length=80)),
                ('appdata', models.CharField(max_length=255)),
                ('amaflags', models.IntegerField()),
                ('accountcode', models.CharField(max_length=20)),
                ('uniqueid', models.CharField(max_length=32)),
                ('linkedid', models.CharField(max_length=32)),
                ('peer', models.CharField(max_length=80)),
                ('userdeftype', models.CharField(max_length=255)),
                ('extra', models.CharField(max_length=512)),
            ],
            options={
                'db_table': 'cel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IvrDetails',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('announcement', models.IntegerField(blank=True, null=True)),
                ('directdial', models.CharField(blank=True, max_length=50, null=True)),
                ('invalid_loops', models.CharField(blank=True, max_length=10, null=True)),
                ('invalid_retry_recording', models.CharField(blank=True, max_length=25, null=True)),
                ('invalid_destination', models.CharField(blank=True, max_length=50, null=True)),
                ('timeout_enabled', models.CharField(blank=True, max_length=50, null=True)),
                ('invalid_recording', models.CharField(blank=True, max_length=25, null=True)),
                ('retvm', models.CharField(blank=True, max_length=8, null=True)),
                ('timeout_time', models.IntegerField(blank=True, null=True)),
                ('timeout_recording', models.CharField(blank=True, max_length=25, null=True)),
                ('timeout_retry_recording', models.CharField(blank=True, max_length=25, null=True)),
                ('timeout_destination', models.CharField(blank=True, max_length=50, null=True)),
                ('timeout_loops', models.CharField(blank=True, max_length=10, null=True)),
                ('timeout_append_announce', models.IntegerField()),
                ('invalid_append_announce', models.IntegerField()),
                ('timeout_ivr_ret', models.IntegerField()),
                ('invalid_ivr_ret', models.IntegerField()),
                ('alertinfo', models.CharField(blank=True, max_length=150, null=True)),
                ('rvolume', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'ivr_details',
                'managed': False,
            },
        ),
    ]