from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from keyboards.user import main_menu
from filters import IsNotAdmin

router = Router()

@router.message(Command("start"), IsNotAdmin())
async def start_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Assalomu alaykum, xush kelibsiz!", reply_markup=main_menu)

@router.message(F.text == "Bekor qilish", IsNotAdmin())
async def cancel_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Bekor qilindi.", reply_markup=main_menu)