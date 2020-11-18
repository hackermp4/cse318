# Generated by Django 2.2.1 on 2020-11-12 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(max_length=50, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(default=None, max_length=255)),
                ('mobile', models.CharField(default=None, max_length=100, null=True)),
                ('password', models.CharField(default=None, max_length=255)),
            ],
            options={
                'db_table': 'students',
            },
        ),
        migrations.DeleteModel(
            name='Clients',
        ),
    ]
