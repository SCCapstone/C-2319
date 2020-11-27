# Generated by Django 3.1.3 on 2020-11-27 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0050_auto_20201127_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(2, 'Used - Good'), (4, 'Used - Not Usable'), (3, 'Used - Poor Condidtion'), (0, 'Brand New'), (1, 'Used - Like New')], default=4),
        ),
    ]
