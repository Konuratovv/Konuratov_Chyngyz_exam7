# Generated by Django 4.2.2 on 2023-07-01 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestbook',
            name='status',
            field=models.CharField(choices=[('Active', 'Активно'), ('Blocked', 'Заблокировано')], default='Active', max_length=50, verbose_name='Статус'),
        ),
    ]
