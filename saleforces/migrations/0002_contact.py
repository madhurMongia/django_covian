# Generated by Django 4.0.1 on 2022-01-10 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saleforces', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('AccountId', models.CharField(max_length=250, null=True)),
                ('Email', models.CharField(max_length=250, null=True)),
                ('FirstName', models.CharField(max_length=250, null=True)),
                ('LastName', models.CharField(max_length=250, null=True)),
                ('Id', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('Phone', models.IntegerField(max_length=250, null=True)),
            ],
        ),
    ]
