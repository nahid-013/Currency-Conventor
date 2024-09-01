# Библеотека
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import math
from aiogram.filters import or_f
from aiogram.types import CallbackQuery,Message
from aiogram import F, Router

# Модули
from Data.request_currency.request_currency import get_dans
from bot_create import bot

# Клавиатуры
from Keyboards.Inline.conversion import all_currency
from Keyboards.Inline.conversion import convertion
from Keyboards.Inline.backs_in_convertion import reset_currency2, reset_currency1

convertion_procces = Router()


class Convertion(StatesGroup):
    currency1 = State()
    currency2 = State()
    count = State()

@convertion_procces.callback_query(F.data.in_({'convert_pair', 'reset_currency1'}))
async def start_fsm(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'reset_currency1':
        await state.clear()
    await callback.answer()
    await state.set_state(Convertion.currency1)
    await callback.message.edit_text(text='Выберите валюту, которую хотите обменять', reply_markup= await convertion('from', 'to_pairs'))

@convertion_procces.callback_query(or_f(Convertion.currency1, F.data.startswith('convertion_from'), F.data == 'reset_currency2'))
async def set_currency1(callback: CallbackQuery, state: FSMContext):
    if callback.data.startswith("convertion_from"):
        global valut
        valut = callback.data[-3:]
    await state.set_state(Convertion.currency1)
    await callback.answer()
    await state.update_data(currency1=valut)
    data = await state.get_data()
    await state.set_state(Convertion.currency2)
    await callback.message.edit_text(text=f'Выберите валюту, на которую хотите обменять <b>{data["currency1"]}</b>',
                                     reply_markup= await convertion('to', 'reset_currency1'), parse_mode='HTML')


@convertion_procces.callback_query(Convertion.currency2, F.data.startswith('convertion_to'))
async def set_currency2(callback: CallbackQuery, state: FSMContext):
    global set_msg
    await callback.answer()
    await state.update_data(currency2=callback.data[-3:])
    await state.set_state(Convertion.count)
    data = await state.get_data()
    set_msg = await callback.message.edit_text(text=f'Введите нужную сумму для обмена\n\n'
                                          f'Курс: {all_currency[data["currency1"]]} {data["currency1"]} = '
                                          f'{get_dans(data["currency1"], data["currency2"])}'
                                          f' {all_currency[data["currency2"]]} {data["currency2"]}',
                                          reply_markup= reset_currency2)

ct = 1
set_msg2 = 0
@convertion_procces.message(Convertion.count)
async def set_count(message: Message, state: FSMContext):
    check_count = message.text.replace(' ', '',).replace(',','').replace('.', '')
    if not check_count.isdigit():
        await message.answer('Введите число')
    else:
        global ct , set_msg2

        if ct:
            await bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=set_msg.message_id, reply_markup=None)
            ct-=1

        if set_msg2:
            await bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=set_msg2.message_id, reply_markup=None)
        else: set_msg2+=1

        await state.update_data(count=check_count)
        data = await state.get_data()
        set_msg2 = await message.answer(f'Можете ввести другю сумму\n\n'
                             f'{all_currency[data["currency1"]]} {data["currency1"]} {check_count} = '
                             f'{round(get_dans(data["currency1"], data["currency2"])  * int(data["count"]), 2)} '
                             f'{all_currency[data["currency2"]]} {data["currency2"]}',
                             reply_markup=reset_currency1)

@convertion_procces.callback_query(F.data == 'finish_convertion')
async def set_count(callback: CallbackQuery, state: FSMContext):
    await state.clear()

