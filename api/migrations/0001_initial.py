# Generated by Django 3.1.1 on 2020-10-04 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('times', models.IntegerField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
