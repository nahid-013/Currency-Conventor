# Библеотека
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, or_f, Command
from aiogram import F, Router

# Модули
from Keyboards.Inline.choose_curr_pairs_k import choose_curr_pairs_k

start_cmd = Router()

@start_cmd.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет, <b>{message.from_user.first_name}</b>\n\n'
                             f'Я помогу узнать актуальные курсы валют.\n'
                             f'Для начала нажмите 👇:', parse_mode='HTML', reply_markup=choose_curr_pairs_k)


@start_cmd.callback_query(F.data.in_({"to_pairs", "finish_convertion"}))
async def cmd_currency(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text='Для начало нажмите: 👇', reply_markup=choose_curr_pairs_k)
