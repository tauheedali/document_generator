# Generated by Django 3.1.7 on 2021-03-19 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldtype',
            name='internal_field',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(blank=True, null=True, unique=True, upload_to='uploads/documents'),
        ),
        migrations.AlterField(
            model_name='document',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='documents.template'),
        ),
    ]