# Generated by Django 3.1.5 on 2021-01-25 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20210125_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='uuid',
            field=models.UUIDField(default='610779105f2111ebb31d784f434f97b9', editable=False, primary_key=True, serialize=False),
        ),
    ]
