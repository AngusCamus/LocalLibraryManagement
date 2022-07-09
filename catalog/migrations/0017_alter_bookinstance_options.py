# Generated by Django 4.0.5 on 2022-07-03 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_make_returned', 'Set book as returned'), ('can_see_all_onloan', 'Can see all book instances status on loan'))},
        ),
    ]