# Generated by Django 3.1.5 on 2021-01-24 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bussinesspart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bussinesspart',
            name='uuid',
            field=models.UUIDField(default='c6a81e205e5711eb9a94784f434f97b9', editable=False, primary_key=True, serialize=False),
        ),
    ]
