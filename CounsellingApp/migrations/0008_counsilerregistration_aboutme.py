# Generated by Django 4.2.1 on 2023-07-25 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CounsellingApp', '0007_booking_request_booking_typ'),
    ]

    operations = [
        migrations.AddField(
            model_name='counsilerregistration',
            name='aboutme',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
