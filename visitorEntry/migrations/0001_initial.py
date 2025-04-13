# Generated by Django 5.1.4 on 2025-03-27 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('purpose', models.TextField()),
                ('visit_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
