from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


reset_currency2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🔙 Назад', callback_data='reset_currency2')],
    ]
)
reset_currency1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🔄 Перезапустить', callback_data='reset_currency1')],
        [InlineKeyboardButton(text='⛔️ Завершить', callback_data='finish_convertion')],
    ]
)