import os
from random import randint

import django

from django_project.telegram_bot.users_manage.models import Recipe, Tag
from asgiref.sync import sync_to_async


@sync_to_async
def random_recipe():
    count = Recipe.objects.all().count()
    id = randint(1, count)
    return Recipe.objects.filter(id=id).first()


@sync_to_async
def select_all_tags():
    return Tag.objects.all()


@sync_to_async
def select_recipe_by_tags(tags: list):
    return Recipe.objects.filter(tag__name__in=tags).distinct()


