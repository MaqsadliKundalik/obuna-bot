from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main_menu = ReplyKeyboardBuilder()
main_menu.button(text="Guruhga qo'shilish")
main_menu = main_menu.as_markup(resize_keyboard=True)

cancel_menu = ReplyKeyboardBuilder()
cancel_menu.button(text="Bekor qilish") 
cancel_menu = cancel_menu.as_markup(resize_keyboard=True)