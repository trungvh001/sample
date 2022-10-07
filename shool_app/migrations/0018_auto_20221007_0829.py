# Generated by Django 3.2.15 on 2022-10-07 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shool_app', '0017_rename_studentclass_studentmanagement'),
    ]

    operations = [
        migrations.AddField(
            model_name='khoa',
            name='person',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lop',
            name='person',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lop',
            name='shool',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shool_app.truong'),
        ),
        migrations.AddField(
            model_name='truong',
            name='person',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
