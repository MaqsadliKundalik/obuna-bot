from aiogram import Router, F
from . import start, stats, send, subscribe

router = Router()

router.include_router(start.router)
router.include_router(stats.router)
router.include_router(send.router)
router.include_router(subscribe.router)
