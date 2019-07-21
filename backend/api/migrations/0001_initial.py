# Generated by Django 2.1.3 on 2019-07-20 16:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('photo', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=80)),
                ('rate', models.IntegerField(default=0)),
                ('sex', models.CharField(choices=[('0', 'male'), ('1', 'female')], default='0', max_length=2)),
                ('friendly', models.IntegerField(default=0)),
                ('cheerful', models.IntegerField(default=0)),
                ('smarty', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=0)),
                ('martial', models.CharField(choices=[('0', 'in-a-relationship'), ('1', 'single')], default='1', max_length=2)),
                ('bio', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=500)),
                ('reviewee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewees', to='api.Profile')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewers', to='api.Profile')),
            ],
        ),
    ]
