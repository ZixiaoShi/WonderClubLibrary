# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('start_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default=b'author', max_length=255),
        ),
        migrations.AddField(
            model_name='book',
            name='donor',
            field=models.ForeignKey(related_name='donor', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='local_avail',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='book',
            name='notes',
            field=models.CharField(max_length=1024, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='pool_date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='pubdate',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='recommender',
            field=models.ManyToManyField(related_name='recommender', null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='renter',
            field=models.ForeignKey(related_name='renter', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.CharField(max_length=1024, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='translator',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='alt_title',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(default=b'0', max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='sub_title',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='pool',
            field=models.ForeignKey(blank=True, to='library.Pool', null=True),
        ),
    ]
