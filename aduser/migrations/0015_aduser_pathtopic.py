# Generated by Django 2.1.4 on 2019-02-18 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aduser', '0014_aduser_displayname'),
    ]

    operations = [
        migrations.AddField(
            model_name='aduser',
            name='PathToPic',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
