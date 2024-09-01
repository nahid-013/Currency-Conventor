# Библеотеки
import asyncio
from aiogram import Dispatcher
from bot_create import bot


# Роутеры
from Routers.start.start_cmd_r import start_cmd
from Routers.convertion_procces import convertion_procces

# модули.


async def main():

    dp = Dispatcher()

    dp.include_router(start_cmd)
    dp.include_router(convertion_procces)


    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.delete_my_commands()
    # await bot.set_my_commands(commands=bot_cmds_list)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

