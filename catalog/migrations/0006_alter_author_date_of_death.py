# Generated by Django 4.0.5 on 2022-07-02 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_author_date_of_death'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, null=True),
        ),
    ]
