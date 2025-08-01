from aiogram import Bot, Dispatcher
from asyncio import run, create_task
from config import TOKEN    
from tasks import check_subscribes
import handlers
from database import init_db
from logging import basicConfig, INFO

dp = Dispatcher()
dp.include_router(handlers.router)

async def main():
    bot = Bot(token=TOKEN)
    create_task(check_subscribes(bot))
    await init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    basicConfig(level=INFO)
    run(main())