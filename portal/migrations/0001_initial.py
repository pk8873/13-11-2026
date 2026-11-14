# Generated for Bharat LPG Demo.
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="GasProduct",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(blank=True, max_length=240)),
                ("price", models.DecimalField(decimal_places=2, max_digits=9)),
                ("active", models.BooleanField(default=True)),
            ],
            options={"ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="PaymentQR",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(default="Demo QR", max_length=100)),
                ("image", models.ImageField(upload_to="payment_qr/")),
                ("instructions", models.CharField(default="यह केवल परीक्षण QR है। वास्तविक भुगतान न करें।", max_length=240)),
                ("active", models.BooleanField(default=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"verbose_name": "Payment QR Settings", "verbose_name_plural": "Payment QR Settings"},
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("customer_name", models.CharField(max_length=120)),
                ("mobile", models.CharField(max_length=15)),
                ("address", models.TextField()),
                ("amount", models.DecimalField(decimal_places=2, max_digits=9)),
                ("status", models.CharField(choices=[("PENDING", "Pending"), ("APPROVED", "Approved"), ("REJECTED", "Rejected"), ("DELIVERED", "Delivered")], default="PENDING", max_length=12)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("product", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="portal.gasproduct")),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
