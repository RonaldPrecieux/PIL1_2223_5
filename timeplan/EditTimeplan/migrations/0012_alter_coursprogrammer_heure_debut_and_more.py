# Generated by Django 4.2.2 on 2023-06-21 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EditTimeplan', '0011_coursprogrammer_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursprogrammer',
            name='heure_debut',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='coursprogrammer',
            name='heure_fin',
            field=models.TimeField(),
        ),
    ]
