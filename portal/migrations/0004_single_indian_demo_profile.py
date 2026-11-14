from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("portal", "0003_demogasconnection")]

    operations = [
        migrations.AlterField(
            model_name="gascompanytheme",
            name="profile_key",
            field=models.CharField(
                choices=[("indian_style", "Indian LPG Service Demo Profile")],
                default="indian_style",
                max_length=24,
            ),
        ),
    ]
