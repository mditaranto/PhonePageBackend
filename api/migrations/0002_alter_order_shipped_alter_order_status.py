# Generated by Django 5.0.4 on 2024-05-02 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipped',
            field=models.IntegerField(choices=[(0, 'Non spedito'), (1, 'Spedito'), (2, 'Nel negozio')], default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='lav', max_length=4),
        ),
    ]
