# Generated by Django 3.0.3 on 2020-03-01 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_auto_20200301_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(2, 'Used - Good'), (3, 'Used - working'), (4, 'Used - Not Working'), (0, 'Brand New'), (1, 'Used - Like New')], default=4),
        ),
    ]
