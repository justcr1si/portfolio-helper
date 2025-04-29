from aiogram import Router

from handlers.user_handlers.profile import profile_router
from handlers.user_handlers.start import start_router

router = Router()
router.include_router(start_router)
router.include_router(profile_router)
