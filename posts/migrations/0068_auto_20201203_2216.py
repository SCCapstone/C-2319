# Generated by Django 3.0 on 2020-12-04 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0067_auto_20201203_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(2, 'Used - Good'), (3, 'Used - Poor Condidtion'), (4, 'Used - Not Usable'), (0, 'Brand New'), (1, 'Used - Like New')], default=4),
        ),
    ]
