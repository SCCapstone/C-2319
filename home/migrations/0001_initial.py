# Generated by Django 2.2.5 on 2019-10-31 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(max_length=200)),
                ('about_content', models.TextField()),
            ],
        ),
    ]
