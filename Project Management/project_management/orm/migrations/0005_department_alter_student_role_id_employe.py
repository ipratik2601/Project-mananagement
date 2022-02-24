# Generated by Django 4.0.2 on 2022-02-21 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0004_alter_student_role_id_alter_student_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.AlterField(
            model_name='student',
            name='role_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orm.role'),
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('department_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orm.department')),
                ('employee_name', models.CharField(max_length=50)),
                ('employee_phone', models.IntegerField()),
            ],
            options={
                'db_table': 'employe',
            },
            bases=('orm.department',),
        ),
    ]
