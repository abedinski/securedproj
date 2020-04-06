# Generated by Django 3.0.4 on 2020-04-06 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecuredResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(choices=[('1', 'Link'), ('2', 'File')], default='1', max_length=2)),
                ('URL', models.URLField(blank=True)),
                ('File', models.FileField(blank=True, upload_to='')),
                ('UID', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('Status', models.CharField(choices=[('1', 'Active'), ('2', 'Expired')], default='1', max_length=2)),
                ('DateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserStatistics',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='userstat', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('LastUserAgent', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SecuredResourceStatistics',
            fields=[
                ('resource', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='resstat', serialize=False, to='webapp.SecuredResource')),
                ('Date', models.DateField(auto_now_add=True)),
                ('Visited', models.IntegerField(default=0)),
            ],
        ),
    ]
