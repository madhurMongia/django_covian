# Generated by Django 4.0.1 on 2022-01-10 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saleforces', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Phone',
            field=models.CharField(max_length=250, null=True),
        ),
    ]