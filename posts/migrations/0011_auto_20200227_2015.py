# Generated by Django 3.0.3 on 2020-02-28 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20200227_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(3, 'Used - working'), (0, 'Brand New'), (1, 'Used - Like New'), (4, 'Used - Not Working'), (2, 'Used - Good')], default=4),
        ),
    ]
