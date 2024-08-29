from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


all_currency = {'USD': '🇺🇸', 'EUR': '🇪🇺', 'AZN': '🇦🇿',
        'AED': "🇦🇪", 'KZT': '🇰🇿', 'UZS': '🇺🇿',
        'AMD': '🇦🇲','BYN': '🇧🇾','GEL': '🇬🇪',
        'TJS': '🇹🇯','TRY': '🇹🇷','CNY': '🇨🇳',
        'GBP': '🏴󠁧󠁢󠁥󠁮󠁧󠁿' ,'EUR': '🇪🇸','EUR': '🇧🇪',
        'EUR': '🇫🇷','EUR': '🇵🇱','EUR': '🇮🇹',
        'RUB': '🇷🇺'}


async def convertion(direction_, path):
    currencies = InlineKeyboardBuilder()
    for currency in all_currency.items():
        currencies.add(InlineKeyboardButton(text=f'{currency[0]} {currency[1]}', callback_data=f'convertion_{direction_}{currency[0]}'))
    return currencies.adjust(3).row(InlineKeyboardButton(text='Назад', callback_data=path)).as_markup()


