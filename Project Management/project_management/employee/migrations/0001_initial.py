# Generated by Django 4.0.2 on 2022-02-24 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employe_name', models.CharField(max_length=50)),
                ('employe_email', models.EmailField(max_length=254)),
                ('employe_age', models.IntegerField()),
                ('employe_contact', models.IntegerField()),
            ],
            options={
                'db_table': 'employe',
            },
        ),
    ]