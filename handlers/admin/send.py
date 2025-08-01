from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from models import User
from keyboards.admin import admin_menu, cancel_menu
from states import AdminSendState
from asyncio import sleep
from filters import IsAdmin

router = Router()

@router.message(F.text == "Xabar yuborish", IsAdmin())
async def send_message(message: Message, state: FSMContext):
    await message.answer("Xabaringizni yuboring.", reply_markup=cancel_menu)
    await state.set_state(AdminSendState.msg)

@router.message(AdminSendState.msg)
async def handle_message(message: Message, state: FSMContext):
    users = await User.all()
    a = 0
    e = 0
    for user in users:
        try:
            await message.copy_to(user.telegram_id)
            a += 1
            await sleep(0.5)
        except:
            e += 1
            continue
    await message.answer(f"Xabar {a} ta foydalanuvchiga yuborildi, {e} ta foydalanuvchiga xabarni yuborishda xatolik bo'ldi.", reply_markup=admin_menu)
    await state.clear()