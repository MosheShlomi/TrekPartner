# Generated by Django 4.1.5 on 2023-01-22 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treks', '0010_alter_trek_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trek',
            name='category',
            field=models.ManyToManyField(related_name='treks', to='treks.category'),
        ),
    ]