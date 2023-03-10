# Generated by Django 3.2.17 on 2023-02-18 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=3000)),
                ('poster', models.FileField(upload_to='')),
                ('developer', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=3000)),
                ('poster', models.FileField(upload_to='')),
                ('director', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Shows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('poster', models.FileField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.games'),
        ),
        migrations.AddField(
            model_name='review',
            name='show',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.shows'),
        ),
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movies'),
        ),
        migrations.DeleteModel(
            name='MGS',
        ),
    ]
