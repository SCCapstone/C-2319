# Generated by Django 3.0.5 on 2020-07-30 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0035_auto_20200720_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(2, 'Used - Good'), (1, 'Used - Like New'), (4, 'Used - Not Usable'), (0, 'Brand New'), (3, 'Used - Poor Condidtion')], default=4),
        ),
    ]
