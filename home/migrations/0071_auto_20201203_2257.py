# Generated by Django 3.0 on 2020-12-04 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0070_auto_20201203_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.IntegerField(choices=[(3, 'Used - Poor Condidtion'), (4, 'Used - Not Usable'), (2, 'Used - Good'), (1, 'Used - Like New'), (0, 'Brand New')], default=4),
        ),
    ]
