# Generated by Django 3.1.3 on 2020-11-27 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0048_auto_20200730_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.IntegerField(choices=[(4, 'Used - Not Usable'), (1, 'Used - Like New'), (2, 'Used - Good'), (0, 'Brand New'), (3, 'Used - Poor Condidtion')], default=4),
        ),
    ]
