# Generated by Django 2.2.2 on 2019-07-04 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0012_auto_20190704_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintrequest',
            name='image',
            field=models.ImageField(default='maintenance/no_image.jpg', upload_to='maintenance'),
        ),
    ]