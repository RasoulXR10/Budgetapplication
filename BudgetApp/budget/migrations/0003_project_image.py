# Generated by Django 3.0.7 on 2020-06-12 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_auto_20200612_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default='default-project.jpg', upload_to='project_pics'),
        ),
    ]
