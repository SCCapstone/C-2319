# Generated by Django 2.2.6 on 2020-02-02 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200202_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(3, 'Used - working'), (4, 'Used - Not Working'), (2, 'Used - Good'), (1, 'Used - Like New'), (0, 'Brand New')], default=4),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
