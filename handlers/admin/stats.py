from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from models import User
from filters import IsAdmin

router = Router()

@router.message(F.text == "Statistics", IsAdmin())
async def show_statistics(message: Message):
    total_users = await User.all().count()
    subscribed_users = await User.filter(status="subscribed").count()
    cancelled_users = await User.filter(status="cancelled").count()
    finished_users = await User.filter(status="finished").count()
    simple_users = await User.filter(status="simple").count()

    stats_message = (
        f"Jami: {total_users}\n"
        f"Obuna bo'lganlar: {subscribed_users}\n"
        f"Bekor qilinganlar: {cancelled_users}\n"
        f"Yakunlanganlar: {finished_users}\n"
        f"Oddiy foydalanuvchilar: {simple_users}"
    )

    await message.answer(stats_message)