# Generated by Django 5.0.4 on 2024-04-29 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_alter_contact_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='categories',
            name='categories',
            field=models.CharField(blank=True, max_length=255, verbose_name='Categoria'),
        ),
    ]