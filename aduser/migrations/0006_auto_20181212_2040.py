# Generated by Django 2.1.4 on 2018-12-12 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aduser', '0005_adgroups_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adgroups',
            name='group',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
    ]
