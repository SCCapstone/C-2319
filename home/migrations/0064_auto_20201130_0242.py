# Generated by Django 3.0 on 2020-11-30 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0063_auto_20201127_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.IntegerField(choices=[(4, 'Used - Not Usable'), (0, 'Brand New'), (3, 'Used - Poor Condidtion'), (1, 'Used - Like New'), (2, 'Used - Good')], default=4),
        ),
    ]
