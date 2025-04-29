from .throttling import ThrottlingMiddleware


async def register_middleware(dp):
    dp.message.middleware(ThrottlingMiddleware())
