# Generated by Django 3.1.3 on 2020-11-27 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0053_auto_20201127_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.IntegerField(choices=[(0, 'Brand New'), (1, 'Used - Like New'), (3, 'Used - Poor Condidtion'), (4, 'Used - Not Usable'), (2, 'Used - Good')], default=4),
        ),
    ]
