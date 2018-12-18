# Generated by Django 2.1.4 on 2018-12-12 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adgroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='auth.Group')),
                ('groupname', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='aduser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('sid', models.CharField(max_length=46, null=True)),
                ('groups', models.ManyToManyField(to='aduser.adgroups')),
            ],
        ),
        migrations.AddField(
            model_name='adgroups',
            name='user',
            field=models.ManyToManyField(to='aduser.aduser'),
        ),
    ]
