# Generated by Django 3.2.3 on 2021-05-18 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0003_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_at',
            field=models.TextField(default=1621314454.0992293),
        ),
    ]
