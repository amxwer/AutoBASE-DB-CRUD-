# Generated by Django 4.2.6 on 2023-10-11 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('model_car', models.CharField(max_length=20)),
                ('type_car', models.CharField(default='sedan', max_length=12)),
                ('horse_power', models.IntegerField(max_length=4)),
                ('engine_capacity', models.FloatField(max_length=10.0)),
                ('gearbox', models.CharField(max_length=20)),
                ('fuel_grade', models.CharField(max_length=9)),
                ('year_of_release', models.IntegerField(max_length=5)),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
            },
        ),
    ]