# Generated by Django 4.1.7 on 2023-03-26 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("modelapp", "0003_customer_phonenumber"),
    ]

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("firstname", models.CharField(max_length=10)),
                ("lastname", models.CharField(max_length=20)),
                ("age", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Licence",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.CharField(max_length=10)),
                ("validForm", models.DateField()),
                ("validTo", models.DateField()),
                (
                    "person",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="modelapp.person",
                    ),
                ),
            ],
        ),
    ]
