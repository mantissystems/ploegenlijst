# Generated by Django 4.1 on 2022-11-09 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viking', '0008_instromer'),
    ]

    operations = [
        migrations.AddField(
            model_name='kluis',
            name='slot',
            field=models.CharField(choices=[('--', '--'), ('H', 'hang'), ('C', 'cijfer'), ('E', 'eigen')], default='H', max_length=18),
        ),
    ]
