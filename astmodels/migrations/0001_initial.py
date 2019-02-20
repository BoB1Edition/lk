# Generated by Django 2.1.4 on 2019-02-18 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('extension', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('voicemail', models.CharField(blank=True, max_length=50, null=True)),
                ('ringtimer', models.IntegerField(blank=True, null=True)),
                ('noanswer', models.CharField(blank=True, max_length=100, null=True)),
                ('recording', models.CharField(blank=True, max_length=50, null=True)),
                ('outboundcid', models.CharField(blank=True, max_length=50, null=True)),
                ('sipname', models.CharField(blank=True, max_length=50, null=True)),
                ('noanswer_cid', models.CharField(max_length=20)),
                ('busy_cid', models.CharField(max_length=20)),
                ('chanunavail_cid', models.CharField(max_length=20)),
                ('noanswer_dest', models.CharField(max_length=255)),
                ('busy_dest', models.CharField(max_length=255)),
                ('chanunavail_dest', models.CharField(max_length=255)),
                ('mohclass', models.CharField(blank=True, max_length=80, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
