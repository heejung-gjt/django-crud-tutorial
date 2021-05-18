# Generated by Django 3.2.3 on 2021-05-18 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0005_auto_20210518_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_at',
            field=models.TextField(default=1621322124.7752051),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('article', models.ManyToManyField(blank=True, related_name='tag', to='crudapp.Article')),
            ],
        ),
    ]
