# Generated by Django 3.1.6 on 2021-09-09 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20210909_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
