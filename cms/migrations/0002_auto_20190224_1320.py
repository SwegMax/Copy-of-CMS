# Generated by Django 2.1.5 on 2019-02-24 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incident',
            options={'ordering': ['-incident_date']},
        ),
        migrations.AddField(
            model_name='incident',
            name='location',
            field=models.TextField(default='Singapore'),
        ),
        migrations.AddField(
            model_name='incident',
            name='severity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='incident',
            name='incident_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date incident happens'),
        ),
    ]
