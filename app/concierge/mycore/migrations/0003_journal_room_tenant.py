# Generated by Django 3.0.1 on 2020-01-14 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mycore', '0002_delete_tenant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('max_tenants', models.IntegerField(verbose_name='Maximum guests')),
                ('is_free', models.BooleanField(default=True)),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mycore.Tenant')),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenants_count', models.IntegerField(blank=True, null=True)),
                ('check_in_date', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('check_out_date', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycore.Room')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycore.Tenant')),
            ],
        ),
    ]
