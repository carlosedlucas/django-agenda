# Generated by Django 2.2.3 on 2022-11-11 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_auto_20221111_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='mostrar',
            field=models.BooleanField(default=True),
        ),
    ]
