# Generated by Django 4.2.16 on 2024-11-07 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='projects',
            field=models.ManyToManyField(related_name='tags', to='app.project'),
        ),
    ]
