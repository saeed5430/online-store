# Generated by Django 5.1.2 on 2025-03-21 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0004_articlecategory_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlecategory',
            old_name='url',
            new_name='url_title',
        ),
    ]
