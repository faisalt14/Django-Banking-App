# Generated by Django 4.1.7 on 2023-02-26 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0006_alter_branch_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='capacity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
