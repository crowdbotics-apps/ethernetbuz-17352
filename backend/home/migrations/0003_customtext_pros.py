# Generated by Django 2.2.12 on 2020-05-25 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='pros',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]