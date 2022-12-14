from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher import FSMContext

from tgbot.keyboards.inline import kb_tags, tag_callback
from tgbot.misc.states import ChooseTags
from tgbot.services.db_commands import select_all_tags, select_recipe_by_tags
from tgbot.services.support_func import send_recipe
from tgbot.services.db_commands import random_recipe as rr


async def start(message: types.Message):
    await message.answer('Привет!'
                         '\n'
                         '\nЯ <b>Общажный бот</b> и я могу подсказать, что тебе приготовить.'
                         '\n'
                         '\n/random_recipe - случайный рецепт'
                         '\n/tags_recipe - рецепты по тегам')


async def random_recipe(message: types.Message):
    recipe = await rr()
    await send_recipe(message.from_user.id, recipe)


async def tags_recipe(message: types.Message):
    keyboard_tags = await kb_tags()
    await message.answer('<b>Выбранные теги:</b>', reply_markup=keyboard_tags)
    await ChooseTags.tags.set()


async def delete_tag_to_recipe(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        if data:
            await call.answer()
            del data['tags'][-1]
            keyboard_tags = await kb_tags(data['tags'])
            await call.message.edit_text(f'<b>Выбранные теги:</b> '
                                         f'{", ".join(data["tags"])}', reply_markup=keyboard_tags)
        else:
            await call.answer(text='Нечего удалять')


async def add_tag_to_recipe(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    value = callback_data['value']
    async with state.proxy() as data:
        if data:
            data['tags'].append(value)
        else:
            data['tags'] = [value]
        keyboard_tags = await kb_tags(data['tags'])
        await call.message.edit_text(f'<b>Выбранные теги:</b> '
                                     f'{", ".join(data["tags"])}', reply_markup=keyboard_tags)


async def find_tag_recipe(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.delete()
    id = call.from_user.id
    async with state.proxy() as data:
        for recipe in await select_recipe_by_tags(data['tags']):
            await send_recipe(id, recipe)
    await state.finish()


def register_user(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(random_recipe, commands=['random_recipe'])
    dp.register_message_handler(tags_recipe, commands=['tags_recipe'])
    dp.register_callback_query_handler(delete_tag_to_recipe, tag_callback.filter(action='удаление'),
                                       state=ChooseTags.tags)
    dp.register_callback_query_handler(add_tag_to_recipe, tag_callback.filter(action='добавление'),
                                       state=ChooseTags.tags)
    dp.register_callback_query_handler(find_tag_recipe, tag_callback.filter(action='поиск'),
                                       state=ChooseTags.tags)
