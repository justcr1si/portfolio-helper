import os
from typing import List

from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT_TOKEN: str = os.getenv('BOT_TOKEN')
    ADMINS: List[str] = ['@' + admin for admin in os.getenv('ADMINS').split(',')] if os.getenv('ADMINS') else []
    DATABASE_NAME: str = os.getenv('DATABASE_NAME')
    BUTTON_COMMANDS: List[str] = [
        '💰 Пополнить баланс',
        '👤 Личный кабинет',
        '🔙 Назад',
    ]

    class Bot:
        title: str = 'PortfolioHelper'
        description: str = 'Telegram bot for portfolio'
        version: str = '0.1.0'


config = Config()
