# Generated by Django 2.1.4 on 2018-12-27 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aduser', '0013_auto_20181214_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='aduser',
            name='DisplayName',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
