# Generated by Django 2.0.3 on 2018-03-22 06:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180322_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issueinvoice',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
