# Generated by Django 4.2.16 on 2024-11-05 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_project_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]
