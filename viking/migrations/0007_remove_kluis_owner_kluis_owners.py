# Generated by Django 4.1 on 2022-11-04 12:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('viking', '0006_alter_kluis_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kluis',
            name='owner',
        ),
        migrations.AddField(
            model_name='kluis',
            name='owners',
            field=models.ManyToManyField(blank=True, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
