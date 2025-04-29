from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_menu():
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='💰 Пополнить баланс')],
        [KeyboardButton(text='👤 Личный кабинет')],
    ], resize_keyboard=True)
    return keyboard


def get_cancel_keyboard():
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='🔙 Назад')],
    ], resize_keyboard=True)
    return keyboard
