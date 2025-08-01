from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from models import User
from config import GROUP_ID
from filters import IsAdmin

router = Router()

@router.callback_query(F.data.startswith("confirm:"), IsAdmin())
async def confirm_subscription(callback_query: CallbackQuery):
    user_id = callback_query.data.split(":")[1]
    
    chat = await callback_query.bot.get_chat(GROUP_ID)
    if not chat:
        await callback_query.answer("Guruh topilmadi.", show_alert=True)
        return
    new_link = await chat.create_invite_link(name=f"Subscription-{user_id}", expire_date=None, member_limit=1)
    
    user = await User.get(telegram_id=int(user_id))
    user.status = "subscribed"
    await user.save()
    
    await callback_query.bot.send_message(
        chat_id=user.telegram_id,
        text=f"Sizning obunangiz tasdiqlandi! Endi siz guruhga qo'shilishingiz mumkin.\n\n{new_link.invite_link}",
    )
    
    
    await callback_query.message.edit_reply_markup(reply_markup=None)
    await callback_query.answer("Obuna tasdiqlandi.")

@router.callback_query(F.data.startswith("cancel:"), IsAdmin())
async def cancel_subscription(callback_query: CallbackQuery):
    user_id = callback_query.data.split(":")[1]
    
    user = await User.get(telegram_id=int(user_id))
    user.status = "cancelled"
    await user.save()
    
    await callback_query.bot.send_message(
        chat_id=user.telegram_id,
        text="Sizning so'rovingiz bekor qilindi.",
    )
    
    await callback_query.message.edit_reply_markup(reply_markup=None)
    await callback_query.answer("So'rov bekor qilindi.")