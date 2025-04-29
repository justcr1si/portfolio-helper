import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from config import config
from database.connector import init_db
from handlers import router
from middlewares import register_middleware


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
        filename='bot.log'
    )

    bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()

    await register_middleware(dp)

    dp.include_router(router)

    await init_db()

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
