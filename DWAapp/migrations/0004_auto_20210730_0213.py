# Generated by Django 3.2.3 on 2021-07-30 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DWAapp', '0003_students'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]
