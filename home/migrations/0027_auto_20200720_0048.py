# Generated by Django 3.0.5 on 2020-07-20 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20200720_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.IntegerField(choices=[(2, 'Used - Good'), (0, 'Brand New'), (3, 'Used - Poor Condidtion'), (4, 'Used - Not Usable'), (1, 'Used - Like New')], default=4),
        ),
    ]
