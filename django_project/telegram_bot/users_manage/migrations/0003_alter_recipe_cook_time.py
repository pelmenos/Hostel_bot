# Generated by Django 4.1.2 on 2022-10-25 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_manage', '0002_alter_recipe_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cook_time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
