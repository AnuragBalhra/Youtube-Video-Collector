# Generated by Django 2.2.6 on 2021-07-09 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=40, unique=True)),
                ('etag', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('channel_id', models.CharField(max_length=50)),
                ('channel_title', models.CharField(max_length=100)),
                ('live_brodcast_content', models.CharField(max_length=50)),
                ('published_at', models.DateTimeField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('default', 'default'), ('medium', 'medium'), ('high', 'high')], max_length=20)),
                ('url', models.URLField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Video')),
            ],
        ),
    ]
