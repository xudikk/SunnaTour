# Generated by Django 4.1.5 on 2023-01-24 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servertokens',
            name='token',
            field=models.TextField(),
        ),
    ]
