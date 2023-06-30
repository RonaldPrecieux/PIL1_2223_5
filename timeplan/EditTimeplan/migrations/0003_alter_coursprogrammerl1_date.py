# Generated by Django 4.2.2 on 2023-06-29 22:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("EditTimeplan", "0002_coursprogrammer_coursprogrammerl1_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coursprogrammerl1",
            name="Date",
            field=models.CharField(
                default="10/05/2023",
                max_length=128,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Le format de date doit être jj/mm/aaaa.",
                        regex="^\\d{2}/\\d{2}/\\d{4}$",
                    )
                ],
            ),
        ),
    ]
