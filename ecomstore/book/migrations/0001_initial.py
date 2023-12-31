# Generated by Django 4.2.1 on 2023-07-03 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.FloatField(blank=True, null=True)),
                ('image_url', models.ImageField(upload_to='pics')),
                ('book_available', models.BooleanField()),
            ],
        ),
    ]
