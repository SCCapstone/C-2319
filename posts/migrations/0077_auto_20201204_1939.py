# Generated by Django 3.0 on 2020-12-05 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0076_auto_20201204_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(2, 'Used - Good'), (1, 'Used - Like New'), (3, 'Used - Poor Condidtion'), (0, 'Brand New'), (4, 'Used - Not Usable')], default=4),
        ),
    ]
