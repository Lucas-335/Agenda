# Generated by Django 5.0.4 on 2024-05-07 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_alter_contact_email_alter_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto'),
        ),
    ]
