# Generated by Django 4.0.5 on 2022-07-03 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0014_remove_book_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='borrowed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
