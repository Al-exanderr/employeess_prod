# Generated by Django 3.1.6 on 2021-09-07 18:08

from django.db import migrations, models
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='man',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('patronymic', models.CharField(max_length=30)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('record_creation_date', models.DateField(default=django.utils.timezone.now)),
                ('reg_number', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
