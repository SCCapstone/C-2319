# Generated by Django 3.0 on 2020-12-04 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0069_auto_20201203_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.IntegerField(choices=[(3, 'Used - Poor Condidtion'), (2, 'Used - Good'), (0, 'Brand New'), (1, 'Used - Like New'), (4, 'Used - Not Usable')], default=4),
        ),
    ]
