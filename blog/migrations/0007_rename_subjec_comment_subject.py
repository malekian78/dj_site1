# Generated by Django 4.2.9 on 2024-02-24 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='subjec',
            new_name='subject',
        ),
    ]