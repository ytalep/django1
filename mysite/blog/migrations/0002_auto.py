# Generated by Django 2.1.3 on 2018-11-09 16:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=200)),
                ('año', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('numerodepuertas', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('precio', models.CharField(max_length=200)),
            ],
        ),
    ]
