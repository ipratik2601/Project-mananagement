# Generated by Django 4.0.2 on 2022-02-21 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('student_email', models.CharField(max_length=50)),
                ('student_password', models.CharField(max_length=50)),
                ('student_phone', models.IntegerField()),
                ('student_address', models.CharField(max_length=50)),
                ('student_dob', models.DateField()),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orm.role')),
            ],
        ),
    ]
