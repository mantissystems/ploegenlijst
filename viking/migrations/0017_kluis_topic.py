# Generated by Django 4.1 on 2022-12-16 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viking', '0016_remove_flexevent_host_remove_flexevent_lid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kluis',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='viking.topic'),
        ),
    ]
