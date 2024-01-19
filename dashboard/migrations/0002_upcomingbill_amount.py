# Generated by Django 5.0.1 on 2024-01-19 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcomingbill',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
            preserve_default=False,
        ),
    ]
