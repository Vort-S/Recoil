# Generated by Django 5.1.1 on 2024-09-18 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choices',
            new_name='Choice',
        ),
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='pub_text',
            new_name='pub_date',
        ),
    ]