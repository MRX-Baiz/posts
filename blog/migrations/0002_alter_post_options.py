# Generated by Django 5.0.3 on 2024-03-29 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-date_created',)},
        ),
    ]