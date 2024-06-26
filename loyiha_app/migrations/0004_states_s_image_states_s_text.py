# Generated by Django 5.0.6 on 2024-05-19 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyiha_app', '0003_states'),
    ]

    operations = [
        migrations.AddField(
            model_name='states',
            name='s_image',
            field=models.ImageField(null=True, upload_to='country_image'),
        ),
        migrations.AddField(
            model_name='states',
            name='s_text',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]
