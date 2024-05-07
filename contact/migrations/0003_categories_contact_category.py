# Generated by Django 5.0.4 on 2024-04-29 19:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_email_alter_contact_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='contact.categories'),
        ),
    ]