# Generated by Django 3.2.6 on 2021-08-20 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('variables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(blank=True, default=None, null=True)),
                ('unit', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
                ('variable', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='variables.variable')),
            ],
        ),
    ]
