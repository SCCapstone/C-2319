# Generated by Django 2.2.6 on 2019-12-05 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0024_auto_20191204_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(0, 'Brand New'), (3, 'Used - working'), (1, 'Used - Like New'), (2, 'Used - Good'), (4, 'Used - Not Working')], default=4),
        ),
    ]
