# Generated by Django 4.0.5 on 2022-07-01 23:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationsRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.CharField(max_length=50)),
                ('stream_id', models.CharField(max_length=50)),
                ('message', models.JSONField(default=dict)),
                ('destination', models.CharField(max_length=200)),
                ('source_service', models.CharField(max_length=50)),
                ('notification_type', models.CharField(max_length=50)),
                ('channel', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('type', models.CharField(max_length=30)),
                ('sub_type', models.CharField(blank=True, max_length=30, null=True)),
                ('link', models.CharField(max_length=255, verbose_name='The link associated')),
                ('image', models.ImageField(upload_to='notifications')),
                ('actions', models.JSONField(default=dict)),
                ('data', models.JSONField(default=dict)),
                ('read', models.DateTimeField(blank=True, null=True)),
                ('sent', models.DateTimeField(auto_now_add=True)),
                ('mode', models.CharField(choices=[('client', 'client'), ('shop', 'shop'), ('admin', 'admin')], default='client', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
