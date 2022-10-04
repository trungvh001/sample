# Generated by Django 3.2.16 on 2022-10-04 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shool_app', '0008_khoa_lop_truong'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_student',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_teacher',
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, choices=[('01', 'student'), ('02', 'teacher')], max_length=3, null=True),
        ),
    ]
