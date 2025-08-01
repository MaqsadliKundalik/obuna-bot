from aiogram import Bot
from models import User
from asyncio import sleep
from datetime import datetime, timedelta
from config import SUBSCRIBE_DAY, GROUP_ID

async def check_subscribes(bot: Bot):
    while True:
        users = await User.filter(status="subscribed").all()
        try:
            chat = await bot.get_chat(GROUP_ID)
        except Exception as e:
            print(f"Error getting chat {GROUP_ID}: {e}")
            await sleep(30)
            continue
        now = datetime.now()
        for user in users:
            days_subscribed = (now - user.updated_at).days

            if days_subscribed > SUBSCRIBE_DAY:
                user.status = "finished"
                await user.save()
                member = await chat.get_member(user.telegram_id)
                if member.status == "member":
                    try:
                        await chat.ban(user.telegram_id)
                        await chat.unban(user.telegram_id)
                        await bot.send_message(
                            user.telegram_id,
                            "Obunangiz muddati tugadi. Iltimos, yangilang.",
                        )
                    except Exception as e:
                        print(f"Error banning/unbanning user {user.telegram_id}: {e}")
            elif SUBSCRIBE_DAY - 5 <= days_subscribed < SUBSCRIBE_DAY:
                days_left = SUBSCRIBE_DAY - days_subscribed
                if days_left in [5, 4, 3, 2, 1]:
                    await bot.send_message(
                        user.telegram_id,
                        f"Obunangiz tugashiga {days_left} kun qoldi."
                    )
            elif days_subscribed == SUBSCRIBE_DAY:
                await bot.send_message(
                    user.telegram_id,
                    "Obunangiz muddati ertaga tugaydi. Iltimos, yangilang."
                )
        await sleep(21600)