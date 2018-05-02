# Generated by Django 2.0.3 on 2018-03-30 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('web_app', '0003_vehicle_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'mission',
            },
        ),
        migrations.AddField(
            model_name='vehicle',
            name='driver',
            field=models.ForeignKey(null=True, on_delete='CASCADE', to='account.Profile'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='mission',
            field=models.ForeignKey(null=True, on_delete='CASCADE', to='web_app.Mission'),
        ),
    ]
