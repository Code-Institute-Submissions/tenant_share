# Generated by Django 2.2.2 on 2019-07-02 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0010_auto_20190701_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintrequest',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]
