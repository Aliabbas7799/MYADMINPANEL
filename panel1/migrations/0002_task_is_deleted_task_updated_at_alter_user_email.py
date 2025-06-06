# Generated by Django 5.1.6 on 2025-05-29 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
