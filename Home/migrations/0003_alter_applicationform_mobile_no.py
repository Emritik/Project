# Generated by Django 4.2.7 on 2023-12-14 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_alter_applicationform_mobile_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='Mobile_No',
            field=models.CharField(max_length=12),
        ),
    ]
