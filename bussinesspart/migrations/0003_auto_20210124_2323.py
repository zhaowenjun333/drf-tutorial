# Generated by Django 3.1.5 on 2021-01-24 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bussinesspart', '0002_auto_20210124_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bussinesspart',
            name='uuid',
            field=models.TextField(default='1a3bcc3a5e5811eb8b0b784f434f97b9', editable=False, primary_key=True, serialize=False),
        ),
    ]
