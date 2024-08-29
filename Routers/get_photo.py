# # Библеотека
# from aiogram.types import Message
# from aiogram import F, Router
# from Bot import bot
#
# # Модули
# from DataBase.requests import register_photo
#
# get_photo = Router()
#
# @get_photo.message(F.photo)
# async def send_photo_bd(message: Message):
#     await register_photo(tg_id=message.from_user.id, name=message.from_user.first_name, photo=message.photo[-1].file_id)
#     # await bot.send_photo(chat_id=880812399, photo=message.photo[-1].file_id)

