# Generated by Django 3.1.3 on 2020-11-27 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0054_auto_20201127_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(3, 'Used - Poor Condidtion'), (0, 'Brand New'), (4, 'Used - Not Usable'), (2, 'Used - Good'), (1, 'Used - Like New')], default=4),
        ),
    ]
