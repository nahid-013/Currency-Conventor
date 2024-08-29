# Библеотека
from aiogram.types import CallbackQuery
from aiogram import F, Router


# Модули
from Keyboards.Inline.choose_curr_pairs_k import choose_curr_pairs_k


choose_curr_type_r = Router()

@choose_curr_type_r.callback_query(F.data.in_({'currency', "to_pairs", "finish_convertion"}))
async def cmd_currency(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text='Выберите интересующее', reply_markup=choose_curr_pairs_k)

# @currency.callback_query(F.data.in_({'crypto'}))
# async def cmd_currency(callback: CallbackQuery):
#     await callback.message.delete()
#     await callback.answer()
#     await callback.message.answer(text='Выберите интересующее', reply_markup=crypto_pairs)


