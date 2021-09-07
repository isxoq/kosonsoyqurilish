# Generated by Django 3.2.6 on 2021-08-14 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiyapp', '0002_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=150)),
                ('rasm', models.ImageField(upload_to='rasmlar/list_rasm')),
                ('izoh', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='playlist',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='List',
        ),
        migrations.AddField(
            model_name='flist',
            name='playlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiyapp.playlist'),
        ),
    ]