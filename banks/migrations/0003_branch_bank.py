# Generated by Django 4.1.7 on 2023-02-22 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0002_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='bank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='banks.bank'),
        ),
    ]