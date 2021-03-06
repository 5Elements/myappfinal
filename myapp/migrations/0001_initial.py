# Generated by Django 2.0.2 on 2018-04-07 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('created_at', models.CharField(max_length=200)),
            ],
        ),
    ]
