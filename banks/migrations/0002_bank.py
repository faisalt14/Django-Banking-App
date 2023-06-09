# Generated by Django 4.1.7 on 2023-02-22 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('banks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('swift_code', models.CharField(max_length=100)),
                ('institution_number', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='banks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
