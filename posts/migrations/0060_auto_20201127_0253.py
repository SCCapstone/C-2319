# Generated by Django 3.1.3 on 2020-11-27 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0059_auto_20201127_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(2, 'Used - Good'), (0, 'Brand New'), (3, 'Used - Poor Condidtion'), (1, 'Used - Like New'), (4, 'Used - Not Usable')], default=4),
        ),
    ]
