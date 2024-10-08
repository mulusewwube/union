# Generated by Django 4.1.5 on 2024-08-14 07:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ORDER', '0030_alter_assignment_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editing',
            name='edited_file',
            field=models.FileField(upload_to='editing/'),
        ),
        migrations.CreateModel(
            name='Research_help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=6)),
                ('title', models.CharField(default='not given', max_length=200)),
                ('number_of_pages', models.IntegerField()),
                ('ordered_at', models.DateTimeField(auto_now_add=True)),
                ('abstract', models.FileField(upload_to='Research_help/')),
                ('description', models.TextField()),
                ('accept_terms', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending', max_length=10)),
                ('user_name', models.ForeignKey(default=19, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
