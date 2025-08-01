from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from keyboards.user import main_menu, cancel_menu
from config import CARD_NUMBER, CARD_NAME, PRICE, ADMINS
from states import SubscribeUserState
from keyboards.admin import check_menu
from filters import IsNotAdmin

router = Router()

@router.message(F.text == "Guruhga qo'shilish", IsNotAdmin())
async def subscribe_to_group(message: Message, state: FSMContext):
    await message.answer(f"""
Guruhga qo'shilish uchun quyidagi karta raqamga {PRICE} UZS to'lov qiling va chekni shu yerga yuboring. Karta egasi {CARD_NAME}

```
{CARD_NUMBER}
""")
    await state.set_state(SubscribeUserState.send_check)

@router.message(SubscribeUserState.send_check)
async def f(message: Message, state: FSMContext):
    for admin in ADMINS:
        await message.copy_to(admin, reply_markup=check_menu(message.from_user.id))
    await message.answer("Iltimos kuting. Tez orada adminlarimiz sizni tasdiqlashadi.", reply_markup=main_menu)
    await state.clear()

