# Generated by Django 5.0.1 on 2024-01-21 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_alter_category_name_alter_expense_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name_of_category']},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='name_of_category',
        ),
    ]
