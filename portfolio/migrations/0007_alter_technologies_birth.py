# Generated by Django 4.2.1 on 2023-06-12 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_technologies_delete_tecnologies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technologies',
            name='birth',
            field=models.DateField(),
        ),
    ]
