# Generated by Django 4.1.5 on 2023-01-24 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayt', '0004_alter_news_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarif',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='tarif'),
        ),
    ]
