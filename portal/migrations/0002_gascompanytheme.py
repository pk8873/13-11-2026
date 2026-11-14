from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("portal", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="GasCompanyTheme",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("portal_name", models.CharField(default="Gas Seva Demo", max_length=100)),
                ("tagline", models.CharField(default="Your demo LPG service portal", max_length=180)),
                ("theme_style", models.CharField(choices=[("indigo", "Indigo Corporate"), ("saffron", "Saffron Service"), ("green", "Green Energy"), ("blue", "Blue Utility")], default="indigo", max_length=20)),
                ("support_phone", models.CharField(blank=True, default="1800-000-0000", max_length=30)),
                ("announcement", models.CharField(blank=True, default="Demo portal: services and payment are simulated.", max_length=220)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"verbose_name": "Website Appearance Settings", "verbose_name_plural": "Website Appearance Settings"},
        ),
    ]
