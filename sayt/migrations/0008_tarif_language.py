# Generated by Django 4.1.5 on 2023-01-30 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayt', '0007_tarifbron'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarif',
            name='language',
            field=models.CharField(choices=[('uz', 'uz'), ('ru', 'ru'), ('ru', 'ru')], default=1, max_length=128),
            preserve_default=False,
        ),
    ]
