from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from filters import IsAdmin
from keyboards.admin import admin_menu
from aiogram.fsm.context import FSMContext

router = Router()

@router.message(Command("start"), IsAdmin())
async def start_command(message: Message):
    await message.answer("Assalomu alaykum, admin panelga xush kelibsiz!", reply_markup=admin_menu)

@router.message(F.text == "Bekor qilish", IsAdmin())
async def cancel_command(message: Message, state: FSMContext):
    await message.answer("Bekor qilindi.", reply_markup=admin_menu)
    await state.clear()