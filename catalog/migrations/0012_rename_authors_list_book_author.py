# Generated by Django 4.0.5 on 2022-07-03 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_rename_author_book_authors_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='authors_list',
            new_name='author',
        ),
    ]
