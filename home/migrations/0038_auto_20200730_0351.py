# Generated by Django 3.0.5 on 2020-07-30 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_auto_20200730_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.IntegerField(choices=[(4, 'Used - Not Usable'), (3, 'Used - Poor Condidtion'), (2, 'Used - Good'), (1, 'Used - Like New'), (0, 'Brand New')], default=4),
        ),
    ]
