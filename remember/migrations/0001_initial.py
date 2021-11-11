# Generated by Django 3.0 on 2021-11-11 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RememberPlaceFB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(db_index=True, max_length=5000, unique=True, verbose_name='Address Facebook')),
                ('comment', models.CharField(db_index=True, max_length=5000, verbose_name='Comment Facebook')),
            ],
            options={
                'verbose_name': 'Remember_Place Facebook-[Autofill]',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='RememberPlaceVk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(db_index=True, max_length=5000, unique=True, verbose_name='Address Vk')),
                ('comment', models.CharField(db_index=True, max_length=5000, verbose_name='Comment Vk')),
            ],
            options={
                'verbose_name': 'Remember Vk-[Autofill]',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='UserLogVk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(db_index=True, max_length=1000, unique=True, verbose_name='Fullname VK')),
                ('releted_place', models.ManyToManyField(blank=True, to='remember.RememberPlaceVk')),
            ],
            options={
                'verbose_name': 'User VK-[Autofill]',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='UserLogFB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(db_index=True, max_length=1000, unique=True, verbose_name='Fullname Facebook')),
                ('releted_place', models.ManyToManyField(blank=True, to='remember.RememberPlaceFB')),
            ],
            options={
                'verbose_name': 'User Facebook-[Autofill]',
                'ordering': ['id'],
            },
        ),
    ]