# Generated by Django 4.1.2 on 2023-08-11 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_skill_tech'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='url',
            field=models.CharField(max_length=500, null=True),
        ),
    ]