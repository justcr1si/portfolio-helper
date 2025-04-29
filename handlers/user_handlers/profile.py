from aiogram import Router, F
from aiogram.types import Message

from database.requests import get_user
from handlers.user_handlers.keyboard import get_cancel_keyboard

profile_router = Router()


@profile_router.message(F.text == '👤 Личный кабинет')
async def cmd_profile(message: Message):
    user = await get_user(message.from_user.id)
    if not user:
        return await message.answer('Сначала запустите бота с помощью /start')
    await message.answer(
        f'📌 Ваш профиль:\n\n'
        f'🆔 ID: {user.telegram_id}\n'
        f'👤 Имя: {user.first_name}\n'
        f'📝 Юзернейм: @{user.username if user.username else 'нет'}\n'
        f'🌐 Язык: {user.language}\n'
        f'📅 Дата регистрации: {user.created_at.strftime('%d.%m.%Y %H:%M')}\n\n'
        f'💸 Баланс: {user.balance}₽',
        reply_markup=get_cancel_keyboard()
    )
