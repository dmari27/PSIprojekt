# Generated by Django 3.1.5 on 2021-01-28 04:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Myapplication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wniosek',
            name='skladajacy',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='wnioski', to=settings.AUTH_USER_MODEL),
        ),
    ]
