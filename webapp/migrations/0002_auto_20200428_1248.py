# Generated by Django 3.0.5 on 2020-04-28 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='securedresource',
            old_name='DateTime',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='securedresource',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='securedresourcestatistics',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='securedresourcestatistics',
            old_name='Visited',
            new_name='visited',
        ),
        migrations.RenameField(
            model_name='userstatistics',
            old_name='LastUserAgent',
            new_name='last_user_agent',
        ),
        migrations.RemoveField(
            model_name='securedresource',
            name='File',
        ),
        migrations.RemoveField(
            model_name='securedresource',
            name='Status',
        ),
        migrations.RemoveField(
            model_name='securedresource',
            name='Type',
        ),
        migrations.RemoveField(
            model_name='securedresource',
            name='URL',
        ),
        migrations.AddField(
            model_name='securedresource',
            name='res_file',
            field=models.FileField(blank=True, default='', upload_to='', verbose_name='Resource File'),
        ),
        migrations.AddField(
            model_name='securedresource',
            name='res_type',
            field=models.IntegerField(choices=[(1, 'link'), (2, 'file')], default=1, verbose_name='Resource Type'),
        ),
        migrations.AddField(
            model_name='securedresource',
            name='status',
            field=models.IntegerField(choices=[(1, 'active'), (2, 'expired')], default=1),
        ),
        migrations.AddField(
            model_name='securedresource',
            name='url',
            field=models.URLField(blank=True, default='', verbose_name='Resource URL'),
        ),
        migrations.AlterField(
            model_name='securedresourcestatistics',
            name='resource',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='webapp.SecuredResource'),
        ),
        migrations.AlterField(
            model_name='userstatistics',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_stat', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='securedresource',
            table='secured_resource',
        ),
        migrations.AlterModelTable(
            name='securedresourcestatistics',
            table='secured_resource_statistics',
        ),
        migrations.AlterModelTable(
            name='userstatistics',
            table='user_statistics',
        ),
    ]