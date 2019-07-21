# Generated by Django 2.1.3 on 2019-07-20 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20190720_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='reviewee',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviewees', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviewers', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]