# Generated by Django 3.1.13 on 2021-08-17 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiyapp', '0003_auto_20210814_0857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=200)),
                ('rasm', models.ImageField(upload_to='rasmlar/playlist_rasm')),
                ('sana', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='playlist',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Flist',
        ),
    ]
