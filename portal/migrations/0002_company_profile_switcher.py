from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portal", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="gascompanytheme",
            name="profile_key",
            field=models.CharField(choices=[("indian_style", "Indian-style LPG Demo Profile"), ("bharat_style", "Bharat-style LPG Demo Profile"), ("green_energy", "Green Energy Utility Demo Profile"), ("custom", "Custom Independent Demo Profile")], default="indian_style", max_length=24),
        ),
        migrations.AddField(
            model_name="gascompanytheme",
            name="logo_text",
            field=models.CharField(default="GS", max_length=10),
        ),
        migrations.AddField(
            model_name="gascompanytheme",
            name="logo_image",
            field=models.ImageField(blank=True, help_text="केवल अपना बनाया हुआ या उपयोग की अनुमति वाला Demo logo upload करें। वास्तविक provider का logo नहीं।", upload_to="demo_branding/"),
        ),
        migrations.AddField(
            model_name="gascompanytheme",
            name="hero_title",
            field=models.CharField(default="LPG सेवाएँ, अब एक ही Demo पोर्टल पर", max_length=160),
        ),
        migrations.AddField(
            model_name="gascompanytheme",
            name="hero_description",
            field=models.CharField(default="बुकिंग और सर्विस अनुभव का अभ्यास इस स्वतंत्र Demo वातावरण में करें।", max_length=260),
        ),
        migrations.AddField(
            model_name="gascompanytheme",
            name="nav_home_label",
            field=models.CharField(default="होम", max_length=40),
        ),
        migrations.AddField(
            model_name="gascompanytheme",
            name="nav_services_label",
            field=models.CharField(default="सेवाएँ", max_length=40),
        ),
        migrations.AddField(
            model_name="gascompanytheme",
            name="nav_booking_label",
            field=models.CharField(default="बुकिंग", max_length=40),
        ),
        migrations.AlterField(
            model_name="gascompanytheme",
            name="theme_style",
            field=models.CharField(choices=[("indigo", "Indigo Corporate"), ("saffron", "Saffron Service"), ("green", "Green Energy"), ("blue", "Blue Utility")], default="indigo", max_length=20),
        ),
    ]
