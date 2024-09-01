from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

choose_curr_pairs_k = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🧮 Конвертировать пару', callback_data='convert_pair')],
    ]
)
