# Generated by Django 2.1.3 on 2019-07-20 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hitup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration', models.DateTimeField(auto_now_add=True)),
                ('allow_review', models.DateTimeField(auto_now_add=True)),
                ('acceptance_status', models.BooleanField(default=False)),
                ('hangee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hangees', to='api.Profile')),
                ('hanger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hangers', to='api.Profile')),
            ],
        ),
    ]
