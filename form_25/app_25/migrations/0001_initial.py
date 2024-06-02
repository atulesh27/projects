# Generated by Django 4.1.1 on 2024-04-25 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='form_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('Employeement_type', models.CharField(choices=[('UNEMPLOYEED', 'unemployeed'), ('EMPLOYEED', 'employeed'), ('SERVING', 'serving')], default='EMPLOYEED', max_length=15)),
            ],
        ),
    ]
