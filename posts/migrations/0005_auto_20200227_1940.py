# Generated by Django 3.0.3 on 2020-02-28 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20200226_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(1, 'Used - Like New'), (2, 'Used - Good'), (4, 'Used - Not Working'), (3, 'Used - working'), (0, 'Brand New')], default=4),
        ),
    ]
