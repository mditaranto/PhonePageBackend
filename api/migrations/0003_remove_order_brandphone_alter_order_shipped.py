# Generated by Django 5.0.4 on 2024-05-08 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_order_shipped_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='brandPhone',
        ),
        migrations.AlterField(
            model_name='order',
            name='shipped',
            field=models.CharField(default='no', max_length=3),
        ),
    ]
