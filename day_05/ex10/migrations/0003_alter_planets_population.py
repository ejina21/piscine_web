# Generated by Django 4.0.4 on 2022-05-24 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex10', '0002_alter_people_created_alter_people_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planets',
            name='population',
            field=models.BigIntegerField(null=True),
        ),
    ]
