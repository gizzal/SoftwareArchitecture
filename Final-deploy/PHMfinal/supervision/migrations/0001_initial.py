# Generated by Django 2.0.3 on 2018-04-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OperationalCostSpareParts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField()),
                ('amount', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Money, $')),
            ],
            options={
                'db_table': 'cost_spare_parts',
            },
        ),
        migrations.CreateModel(
            name='OperationalCostWorkload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField()),
                ('amount', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Working Hours')),
            ],
            options={
                'db_table': 'workload_spare_parts',
            },
        ),
    ]
