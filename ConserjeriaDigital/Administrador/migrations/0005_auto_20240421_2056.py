# Generated by Django 3.1.3 on 2024-04-22 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0004_residente_numerodepartamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correspondencia',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]