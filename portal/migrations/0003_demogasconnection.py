from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("portal", "0002_company_profile_switcher")]

    operations = [
        migrations.CreateModel(
            name="DemoGasConnection",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("connection_number", models.CharField(help_text="केवल काल्पनिक Demo ID, जैसे DEMO-100001", max_length=24, unique=True)),
                ("owner_name", models.CharField(help_text="केवल काल्पनिक नाम इस्तेमाल करें।", max_length=120)),
                ("area_label", models.CharField(blank=True, help_text="काल्पनिक क्षेत्र/पता; वास्तविक ग्राहक का पता नहीं।", max_length=120)),
                ("status", models.CharField(choices=[("HOLD", "Demo On Hold"), ("ACTIVE", "Demo Active")], default="HOLD", max_length=10)),
                ("demo_due_amount", models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["connection_number"], "verbose_name": "Demo Gas Connection", "verbose_name_plural": "Demo Gas Connections"},
        ),
    ]
