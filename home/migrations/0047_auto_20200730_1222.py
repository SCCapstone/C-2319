# Generated by Django 3.0.5 on 2020-07-30 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0046_auto_20200730_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.IntegerField(choices=[(3, 'Used - Poor Condidtion'), (4, 'Used - Not Usable'), (1, 'Used - Like New'), (2, 'Used - Good'), (0, 'Brand New')], default=4),
        ),
    ]
