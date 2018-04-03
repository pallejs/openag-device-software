# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-03 21:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20180403_2131'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Environment',
            new_name='EnvironmentModel',
        ),
        migrations.RenameModel(
            old_name='Recipe',
            new_name='RecipeModel',
        ),
        migrations.RenameModel(
            old_name='RecipeTransition',
            new_name='RecipeTransitionModel',
        ),
        migrations.RenameModel(
            old_name='State',
            new_name='StateModel',
        ),
        migrations.AlterModelOptions(
            name='environmentmodel',
            options={'get_latest_by': 'timestamp', 'verbose_name': 'Environment', 'verbose_name_plural': 'Environments'},
        ),
        migrations.AlterModelOptions(
            name='recipemodel',
            options={'verbose_name': 'Recipe', 'verbose_name_plural': 'Recipes'},
        ),
        migrations.AlterModelOptions(
            name='statemodel',
            options={'verbose_name': 'State', 'verbose_name_plural': 'State'},
        ),
    ]
