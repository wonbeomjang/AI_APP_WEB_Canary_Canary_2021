# Generated by Django 3.2.8 on 2021-10-12 13:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('deeplearning', '0004_trainedmodel_matrix'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.CharField(max_length=500)),
                ('create_at', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]