# Generated by Django 4.0.1 on 2022-02-12 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tution', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=191)),
                ('slug', models.CharField(max_length=191)),
                ('email', models.EmailField(max_length=254)),
                ('salary', models.FloatField()),
                ('detail', models.TextField()),
                ('available', models.BooleanField()),
                ('category', models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student')], max_length=191)),
            ],
        ),
    ]
