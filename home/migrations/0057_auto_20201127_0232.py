# Generated by Django 3.1.3 on 2020-11-27 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0056_auto_20201127_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.IntegerField(choices=[(1, 'Used - Like New'), (0, 'Brand New'), (4, 'Used - Not Usable'), (3, 'Used - Poor Condidtion'), (2, 'Used - Good')], default=4),
        ),
    ]
