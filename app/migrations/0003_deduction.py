# Generated by Django 4.1.3 on 2024-07-02 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_rename_lbags_bill_bags"),
    ]

    operations = [
        migrations.CreateModel(
            name="deduction",
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
                ("Cooli_Rent", models.CharField(max_length=100)),
                ("LF_Amount", models.CharField(max_length=100)),
                ("Commission", models.CharField(max_length=100)),
                ("Brokerage", models.CharField(max_length=100)),
            ],
        ),
    ]
