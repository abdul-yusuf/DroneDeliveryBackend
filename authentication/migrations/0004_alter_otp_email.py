# Generated by Django 4.2.2 on 2024-07-30 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0003_remove_otp_user_otp_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="otp",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
