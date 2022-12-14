from aiogram import Bot

from django_project.telegram_bot.config.settings import MEDIA_ROOT
from tgbot.services.db_commands import random_recipe


async def send_recipe(chat_id, recipe):
    bot = Bot.get_current()
    with open(f'{MEDIA_ROOT}/{recipe.picture}', 'rb') as file:
        await bot.send_photo(chat_id, file, caption=await create_caption(recipe))
    message = await create_recipe_for_message(recipe.recipe)
    for x in range(0, len(message), 4096):
        await bot.send_message(chat_id, message[x:x+4096])


async def create_caption(recipe):
    caption = ''
    caption += f'<b>{recipe.title}</b>\n\n'
    if recipe.cook_time:
        caption += f'<b>Время приготовления:</b> {recipe.cook_time} минут\n\n'
    caption += f'<b>Ингридиенты:</b>\n{recipe.products}\n\n'
    caption += f'<b>Теги: {", ".join(list(map(str, recipe.tag.all())))}</b>'
    return caption


async def create_recipe_for_message(recipe):
    message = '<b>Рецепт:</b>\n'
    message += recipe
    return message
