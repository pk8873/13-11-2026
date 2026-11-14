from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portal", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="GasCompanyTheme",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("profile_key", models.CharField(choices=[("indian_style", "Indian-style LPG Demo Profile"), ("bharat_style", "Bharat-style LPG Demo Profile"), ("green_energy", "Green Energy Utility Demo Profile"), ("custom", "Custom Independent Demo Profile")], default="indian_style", max_length=24)),
                ("portal_name", models.CharField(default="Gas Seva Demo", max_length=100)),
                ("logo_text", models.CharField(default="GS", max_length=10)),
                ("logo_image", models.ImageField(blank=True, help_text="केवल अपना बनाया हुआ या उपयोग की अनुमति वाला Demo logo upload करें। वास्तविक provider का logo नहीं।", upload_to="demo_branding/")),
                ("tagline", models.CharField(default="Your independent demo LPG service portal", max_length=180)),
                ("theme_style", models.CharField(choices=[("indigo", "Indigo Corporate"), ("saffron", "Saffron Service"), ("green", "Green Energy"), ("blue", "Blue Utility")], default="indigo", max_length=20)),
                ("hero_title", models.CharField(default="LPG सेवाएँ, अब एक ही Demo पोर्टल पर", max_length=160)),
                ("hero_description", models.CharField(default="बुकिंग और सर्विस अनुभव का अभ्यास इस स्वतंत्र Demo वातावरण में करें।", max_length=260)),
                ("nav_home_label", models.CharField(default="होम", max_length=40)),
                ("nav_services_label", models.CharField(default="सेवाएँ", max_length=40)),
                ("nav_booking_label", models.CharField(default="बुकिंग", max_length=40)),
                ("support_phone", models.CharField(blank=True, default="1800-000-0000", max_length=30)),
                ("announcement", models.CharField(blank=True, default="Demo portal: services and payment are simulated.", max_length=220)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"verbose_name": "Website Company Profile Switcher", "verbose_name_plural": "Website Company Profile Switcher"},
        ),
    ]
