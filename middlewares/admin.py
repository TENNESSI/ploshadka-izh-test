from aiogram import types
from config.settings import config

class AdminMiddleware:
    async def __call__(self, handler, event: types.Message, data):
        if event.from_user.id in config.ADMIN_IDS:
            data['is_admin'] = True
        else:
            data['is_admin'] = False
        return await handler(event, data)