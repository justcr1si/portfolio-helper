from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from handlers.payment.states import PaymentState
from handlers.user_handlers.keyboard import get_cancel_keyboard, get_main_menu

payment_router = Router()


@payment_router.message(F.text == '💰 Пополнить баланс')
async def add_balance(message: Message, state: FSMContext):
    await message.answer(
        'Введите сумму для пополнения (руб):',
        reply_markup=get_cancel_keyboard()
    )
    await state.set_state(PaymentState.waiting_for_payment)


@payment_router.message(PaymentState.waiting_for_payment, F.text)
async def process_payment(message: Message, state: FSMContext):
    try:
        amount = float(message.text)

        await message.answer(
            f'💳 Стоимость пополнения {amount}₽',
            reply_markup=get_cancel_keyboard()
        )
    except ValueError:
        await message.answer(
            'Некорректно введенные данные.\n'
            'Повторите попытку.',
            reply_markup=get_cancel_keyboard()
        )
    finally:
        await state.clear()


@payment_router.message(F.text == '🔙 Назад')
async def cancel_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Главное меню:', reply_markup=get_main_menu())
