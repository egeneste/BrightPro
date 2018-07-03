# Generated by Django 2.0.6 on 2018-06-24 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('staff_team', models.CharField(blank=True, max_length=20)),
                ('staff_rank', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
