# Generated by Django 2.0.5 on 2018-05-23 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderline',
            name='orderid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderlines_relation', to='API.Order'),
        ),
    ]
