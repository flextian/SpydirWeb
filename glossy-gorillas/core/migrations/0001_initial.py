# Generated by Django 3.0.8 on 2020-08-02 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="InventoryRecord",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField(verbose_name="Quantity")),
                (
                    "quantity_type",
                    models.CharField(
                        choices=[
                            ("C", "Count"),
                            ("G", "Weight in Grams"),
                            ("K", "Weight in Kilograms"),
                        ],
                        max_length=3,
                        verbose_name="Quantity Type",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Listing",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "silver_per_unit",
                    models.IntegerField(
                        null=True, verbose_name="Weight in Silver per traded unit"
                    ),
                ),
                (
                    "barter_qty_per_unit",
                    models.IntegerField(
                        null=True, verbose_name="Barter unit(s) per traded unit"
                    ),
                ),
                (
                    "allow_offers",
                    models.BooleanField(
                        default=False, verbose_name="Allow user barter offers"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("A", "Listing Available"),
                            ("N", "In Negotiations"),
                            ("S", "Agreed and Scheduled"),
                            ("F", "Trade Finalized"),
                        ],
                        default="A",
                        max_length=3,
                        verbose_name="Trade Status",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Product Name")),
                (
                    "product_type",
                    models.CharField(
                        choices=[
                            ("service", "Service"),
                            ("spice", "Spice"),
                            ("object", "Object"),
                        ],
                        default="spice",
                        max_length=10,
                        verbose_name="Product Type",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Trader",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField(verbose_name="User Description")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Trade",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "buyer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.Trader",
                        verbose_name="Buyer",
                    ),
                ),
                (
                    "listing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.Listing",
                        verbose_name="Trade Listing",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="listing",
            name="barter_product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.Product",
                verbose_name="Type of product requested for barter",
            ),
        ),
        migrations.AddField(
            model_name="listing",
            name="item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="core.InventoryRecord",
                verbose_name="Listed Item",
            ),
        ),
        migrations.AddField(
            model_name="inventoryrecord",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="core.Trader",
                verbose_name="Owner",
            ),
        ),
        migrations.AddField(
            model_name="inventoryrecord",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="core.Product",
                verbose_name="Product",
            ),
        ),
    ]
