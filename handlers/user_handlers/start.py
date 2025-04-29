from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from database.requests import get_user, create_user

start_router = Router()


@start_router.message(Command('start'))
async def cmd_start(message: Message):
    user = await get_user(message.from_user.id)
    if not user:
        await create_user(
            telegram_id=message.from_user.id,
            first_name=message.from_user.first_name,
            username=message.from_user.username,
            last_name=message.from_user.last_name
        )
    await message.answer(
        f'Привет, {message.from_user.full_name}!\n\n'
        'Это демонстрационный бот для портфолио.\n'
        'Используй /profile чтобы посмотреть свой профиль'
    )
