# Generated by Django 3.0.5 on 2020-07-30 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0042_auto_20200730_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(0, 'Brand New'), (2, 'Used - Good'), (1, 'Used - Like New'), (3, 'Used - Poor Condidtion'), (4, 'Used - Not Usable')], default=4),
        ),
    ]
