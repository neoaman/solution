# Generated by Django 3.2 on 2021-04-09 13:05

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postId', models.CharField(default=blog.models.auto_id, max_length=10, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('subTitle', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('publishDate', models.DateTimeField()),
                ('draft', models.BooleanField()),
                ('tag', models.JSONField()),
                ('content', models.TextField()),
            ],
        ),
    ]
