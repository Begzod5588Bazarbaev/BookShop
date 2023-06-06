# Generated by Django 4.1.7 on 2023-05-30 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('description', models.TextField(max_length=300, verbose_name='Дополнительная информация')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pub_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]