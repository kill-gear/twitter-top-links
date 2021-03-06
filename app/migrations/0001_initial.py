# Generated by Django 3.1.1 on 2020-09-25 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('tweet_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('user_id', models.BigIntegerField()),
                ('user_screen_name', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.BigIntegerField()),
                ('domain_name', models.URLField()),
            ],
            options={
                'unique_together': {('tweet_id', 'domain_name')},
            },
        ),
    ]
