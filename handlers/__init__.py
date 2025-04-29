from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import Message

from config import config
from handlers.payment.payment import payment_router
from handlers.user_handlers.keyboard import get_main_menu
from handlers.user_handlers.profile import profile_router
from handlers.user_handlers.start import start_router

router = Router()
router.include_router(start_router)
router.include_router(profile_router)
router.include_router(payment_router)


@router.message(
    F.text,
    ~(F.text.startswith('/')),
    ~(F.text.in_(config.BUTTON_COMMANDS)),
    StateFilter(None)
)
async def handle_message(message: Message):
    await message.answer(
        'Используйте кнопки для взаимодействия со мной\n',
        reply_markup=get_main_menu()
    )
