# Generated by Django 4.1.5 on 2023-01-31 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayt', '0009_rename_paket_tarif_paket_en_remove_tarif_language_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarif',
            name='paket',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
