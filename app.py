# Библеотеки
import asyncio
from aiogram import Dispatcher
from bot_create import bot


# Роутеры
from Routers.start_cmd_r import start_cmd
from Routers.choose_curr_type_r import choose_curr_type_r
from Routers.choose_curr_pairs_r import choose_curr_pair_r
from Routers.convertion_procces import convertion_procces
from Routers.convertion_crypto_procces import crypto_convertion_procces


# модули.
from  bot_cmds_list import bot_cmds_list


async def main():

    dp = Dispatcher()

    dp.include_router(start_cmd)
    dp.include_router(choose_curr_type_r)
    dp.include_router(choose_curr_pair_r)
    dp.include_router(convertion_procces)
    dp.include_router(crypto_convertion_procces)


    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.delete_my_commands()
    # await bot.set_my_commands(commands=bot_cmds_list)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

