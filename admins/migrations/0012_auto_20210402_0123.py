# Generated by Django 3.1.7 on 2021-04-01 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0011_auto_20210402_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
