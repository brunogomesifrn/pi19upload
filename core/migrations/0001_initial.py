# Generated by Django 2.2.4 on 2019-08-19 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('data', models.DateTimeField(verbose_name='Data')),
                ('arquivo', models.FileField(upload_to='upload', verbose_name='Arquivo')),
                ('local', models.CharField(max_length=100, verbose_name='Local Físico')),
                ('remetente', models.CharField(max_length=100, verbose_name='Remetente')),
            ],
        ),
    ]
