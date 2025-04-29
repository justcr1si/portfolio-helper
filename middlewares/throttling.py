import logging
from datetime import datetime, timedelta

from aiogram import BaseMiddleware
from aiogram.types import Message


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self):
        self.user_timeouts = {}
        self.timeout = 1

    async def __call__(self, handler, event: Message, data):
        user_id = event.from_user.id
        current_time = datetime.now()

        if user_id in self.user_timeouts:
            last_message_time = self.user_timeouts[user_id]
            if current_time - last_message_time < timedelta(seconds=self.timeout):
                logging.warning(f'User {user_id} is flooding')
                await event.answer('Слишком много запросов! Пожалуйста, подождите...')
                return

        self.user_timeouts[user_id] = current_time
        return await handler(event, data)
