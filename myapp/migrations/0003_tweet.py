# Generated by Django 2.0.2 on 2018-04-07 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0002_delete_tweet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tw_text', models.TextField()),
                ('tw_user', models.CharField(max_length=200)),
                ('tw_cat', models.FloatField(max_length=200)),
                ('tw_img_src', models.TextField()),
                ('tw_desc', models.TextField()),
                ('tw_id', models.TextField(unique=True)),
                ('created_at', models.CharField(max_length=200)),
            ],
        ),
    ]
