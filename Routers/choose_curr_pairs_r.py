# Библеотека
from aiogram.types import CallbackQuery
from aiogram import F, Router


# Модули
from Keyboards.Inline.choose_curr_type_k import choose_curr_type_k

choose_curr_pair_r = Router()

# @choose_curr_pair_r.callback_query(F.data.in_({'convert_pair'}))
# async def cmd_currency(callback: CallbackQuery):
#     await callback.answer()
#     await callback.message.edit_text(text='Выберите валюту, которую хотите обменять', reply_markup= await convertion('from'))

# @currency.callback_query(F.data.in_({'favorite'}))
# async def cmd_currency(callback: CallbackQuery):
#     await callback.message.delete()
#     await callback.answer()
#     await callback.message.answer(text='Выберите интересующее', reply_markup=choose_curr_pairs_k)

@choose_curr_pair_r.callback_query(F.data == 'back_to_curr_type')
async def back_cmd_start(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(f'Для начала выберите:', reply_markup=choose_curr_type_k)