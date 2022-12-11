# Generated by Django 4.1.3 on 2022-12-11 12:21

import Public.cache.mixins
import Public.mixins
import Public.models
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=Public.models.upload_image_src)),
                ('link', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ('-id',),
            },
            bases=(Public.cache.mixins.CacheMixin, Public.mixins.RemovePastFileWhenChangedMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('date_time_create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_range', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-id',),
            },
            bases=(Public.cache.mixins.CacheMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_range', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-id',),
            },
            bases=(Public.cache.mixins.CacheMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('work_position', models.CharField(max_length=40)),
                ('about', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to=Public.models.upload_image_src)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('github_id', models.CharField(blank=True, max_length=20, null=True)),
                ('telegram_id', models.CharField(blank=True, max_length=20, null=True)),
                ('instagram_id', models.CharField(blank=True, max_length=20, null=True)),
                ('linkdin_id', models.CharField(blank=True, max_length=20, null=True)),
            ],
            bases=(Public.cache.mixins.CacheMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MessageNotif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_time_send', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_showing', models.BooleanField(default=False)),
                ('image', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ('-id',),
            },
            bases=(Public.cache.mixins.CacheMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('percentage', models.IntegerField()),
                ('is_showing', models.BooleanField(default=True)),
                ('linked', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Public.category')),
            ],
            bases=(Public.cache.mixins.CacheMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TelegramBot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(max_length=20)),
                ('token_bot', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkSample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('views', models.BigIntegerField(default=0)),
                ('date_time_create', models.DateField(auto_now_add=True)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Public.gallery')),
                ('skills', models.ManyToManyField(to='Public.skill')),
            ],
            options={
                'ordering': ('-id',),
            },
            bases=(Public.cache.mixins.CacheMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=Public.models.upload_image_gallery_src)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Public.gallery')),
            ],
            bases=(Public.mixins.RemovePastFileWhenChangedMixin, models.Model),
        ),
    ]
