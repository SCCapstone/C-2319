# Generated by Django 3.0 on 2020-12-04 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0072_auto_20201203_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(3, 'Used - Poor Condidtion'), (2, 'Used - Good'), (0, 'Brand New'), (1, 'Used - Like New'), (4, 'Used - Not Usable')], default=4),
        ),
    ]
