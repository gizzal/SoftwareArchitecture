# Generated by Django 2.0.3 on 2018-04-16 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_config'),
        ('web_app', '0013_auto_20180416_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wind_speed', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('humidity', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('temperature', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('pressure', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('highway', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('surface', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('smoothness', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('tracktype', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('incline', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('length', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('engine_state', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('fuel_state', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('battery_state', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('engine_delta', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('fuel_delta', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('battery_delta', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dataset', to='account.Profile')),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dataset', to='web_app.Mission')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dataset', to='web_app.VehicleType', verbose_name='Vehicle Type')),
            ],
            options={
                'db_table': 'dataset',
            },
        ),
    ]
