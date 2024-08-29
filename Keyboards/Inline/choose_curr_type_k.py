from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

choose_curr_type_k = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='💸 Валюта', callback_data='currency')],
        [InlineKeyboardButton(text='📈 Криптовалюта', callback_data='crypto')],
    ]
)

# async def inline_categories():
#     categories = InlineKeyboardBuilder()
#     for category in await get_category():
#         categories.add(InlineKeyboardButton(text=category.name, callback_data=f'category {category.id}'))
#     return categories.adjust(2).as_markup()