# Библеотека
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, or_f, Command
from aiogram import F, Router

# Модули
from Keyboards.Inline.choose_curr_type_k import choose_curr_type_k

start_cmd = Router()

@start_cmd.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет, <b>{message.from_user.first_name}</b>\n\n'
                             f'Я помогу узнать актуальные курсы валют и криптовалют.\n'
                             f'Для начала выберите:', parse_mode='HTML', reply_markup=choose_curr_type_k)


