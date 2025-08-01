from aiogram import Router
from . import start, subscribe

router = Router()

router.include_router(start.router)
router.include_router(subscribe.router)