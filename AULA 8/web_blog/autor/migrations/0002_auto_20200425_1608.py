# Generated by Django 2.2.11 on 2020-04-25 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterField(
            model_name='autor',
            name='email',
            field=models.EmailField(max_length=240, unique=True),
        ),
    ]