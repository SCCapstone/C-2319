# Generated by Django 2.2.6 on 2020-02-02 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(0, 'Brand New'), (1, 'Used - Like New'), (3, 'Used - working'), (2, 'Used - Good'), (4, 'Used - Not Working')], default=4),
        ),
    ]
