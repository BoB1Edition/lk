# Generated by Django 2.1.4 on 2018-12-12 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aduser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adgroups',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
