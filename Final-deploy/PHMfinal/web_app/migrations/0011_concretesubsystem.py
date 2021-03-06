# Generated by Django 2.0.3 on 2018-04-14 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0010_auto_20180411_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConcreteSubSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health', models.DecimalField(decimal_places=1, max_digits=5)),
                ('subsystem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.SubSystem')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.Vehicle')),
            ],
            options={
                'db_table': 'concrete_sub_sys',
            },
        ),
    ]
