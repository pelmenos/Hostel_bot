from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from tgbot.services.db_commands import select_all_tags


tag_callback = CallbackData('tag', 'action', 'value')


async def kb_tags(tags=None):
    if tags is None:
        tags = []
    btn = InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn.insert(InlineKeyboardButton(text='Убрать последний тег', callback_data=tag_callback.new(action='удаление', value=0)))
    for tag in await select_all_tags():
        if str(tag) not in tags:
            btn.insert(InlineKeyboardButton(text=f'{tag}', callback_data=tag_callback.new(action='добавление', value=tag)))
    btn.insert(InlineKeyboardButton(text='Найти', callback_data=tag_callback.new(action='поиск', value=0)))
    return btn
