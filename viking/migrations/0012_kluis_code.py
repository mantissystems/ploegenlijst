# Generated by Django 4.1 on 2022-11-10 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viking', '0011_alter_kluis_slot'),
    ]

    operations = [
        migrations.AddField(
            model_name='kluis',
            name='code',
            field=models.TextField(blank=True, null=True),
        ),
    ]