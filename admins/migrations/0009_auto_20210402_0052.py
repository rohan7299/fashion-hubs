# Generated by Django 3.1.7 on 2021-04-01 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0008_auto_20210402_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='active',
            field=models.BooleanField(),
        ),
    ]