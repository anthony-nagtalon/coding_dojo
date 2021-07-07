# Generated by Django 2.2.4 on 2021-07-06 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=63)),
                ('last_name', models.CharField(max_length=63)),
                ('email', models.CharField(max_length=255)),
                ('pw_hash', models.CharField(max_length=60)),
            ],
        ),
    ]
