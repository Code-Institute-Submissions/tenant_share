# Generated by Django 2.2.2 on 2019-07-01 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0009_auto_20190701_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintrequest',
            name='image',
            field=models.ImageField(default='mantenance/no_image.jpg', upload_to='maintenance'),
        ),
        migrations.DeleteModel(
            name='MaintRequestImage',
        ),
    ]