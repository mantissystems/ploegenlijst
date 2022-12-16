# Generated by Django 4.1 on 2022-12-16 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viking', '0015_person_lnr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flexevent',
            name='host',
        ),
        migrations.RemoveField(
            model_name='flexevent',
            name='lid',
        ),
        migrations.RemoveField(
            model_name='flexevent',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='flexlid',
            name='flexevent',
        ),
        migrations.RemoveField(
            model_name='flexlid',
            name='member',
        ),
        migrations.RemoveField(
            model_name='person',
            name='pos1',
        ),
        migrations.RemoveField(
            model_name='person',
            name='pos2',
        ),
        migrations.RemoveField(
            model_name='person',
            name='pos3',
        ),
        migrations.RemoveField(
            model_name='person',
            name='pos4',
        ),
        migrations.RemoveField(
            model_name='person',
            name='pos5',
        ),
        migrations.DeleteModel(
            name='Bericht',
        ),
        migrations.DeleteModel(
            name='Flexevent',
        ),
        migrations.DeleteModel(
            name='Flexlid',
        ),
    ]