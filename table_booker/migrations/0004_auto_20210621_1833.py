# Generated by Django 3.0.8 on 2021-06-21 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('table_booker', '0003_auto_20210620_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='setting', to='table_booker.Restaurant'),
        ),
    ]