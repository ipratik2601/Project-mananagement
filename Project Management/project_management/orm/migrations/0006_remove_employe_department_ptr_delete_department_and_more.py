# Generated by Django 4.0.2 on 2022-02-21 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0005_department_alter_student_role_id_employe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employe',
            name='department_ptr',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Employe',
        ),
    ]