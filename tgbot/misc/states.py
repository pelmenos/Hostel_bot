from aiogram.dispatcher.filters.state import StatesGroup, State


class ChooseTags(StatesGroup):
    tags = State()
