# Generated by Django 3.0 on 2020-12-04 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0066_auto_20201203_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.IntegerField(choices=[(1, 'Used - Like New'), (4, 'Used - Not Usable'), (3, 'Used - Poor Condidtion'), (2, 'Used - Good'), (0, 'Brand New')], default=4),
        ),
    ]
