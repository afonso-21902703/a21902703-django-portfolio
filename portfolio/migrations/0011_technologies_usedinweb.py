# Generated by Django 4.2.1 on 2023-06-14 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_patterns_technologies_usedesc'),
    ]

    operations = [
        migrations.AddField(
            model_name='technologies',
            name='usedInWeb',
            field=models.BooleanField(default=False),
        ),
    ]
