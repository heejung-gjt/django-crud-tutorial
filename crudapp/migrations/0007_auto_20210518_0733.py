# Generated by Django 3.2.3 on 2021-05-18 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0006_auto_20210518_0715'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='article',
            new_name='articles',
        ),
        migrations.AlterField(
            model_name='article',
            name='create_at',
            field=models.TextField(default=1621323185.6262977),
        ),
    ]
