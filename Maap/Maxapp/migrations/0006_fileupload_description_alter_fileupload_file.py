# Generated by Django 5.0 on 2024-02-01 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maxapp', '0005_fileupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='description',
            field=models.CharField(default='File has no description', max_length=1000),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='file',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
