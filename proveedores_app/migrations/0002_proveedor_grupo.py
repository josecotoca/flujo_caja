# Generated by Django 5.1.7 on 2025-03-27 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='grupo',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
