# Generated by Django 2.1.4 on 2019-02-21 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aduser', '0015_aduser_pathtopic'),
    ]

    operations = [
        migrations.AddField(
            model_name='aduser',
            name='Description',
            field=models.TextField(null=True),
        ),
    ]