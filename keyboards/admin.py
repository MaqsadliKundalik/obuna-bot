from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

def check_menu(user_id):
    markup = InlineKeyboardBuilder()
    markup.button(text="Tasdi1qlash", callback_data=f"confirm:{user_id}")
    markup.button(text="Rad etish", callback_data=f"cancel:{user_id}")
    markup.adjust(1)
    return markup.as_markup()

admin_menu = ReplyKeyboardBuilder()
admin_menu.button(text="Statistika")
admin_menu.button(text="Xabar yuborish")
admin_menu.adjust(2)
admin_menu = admin_menu.as_markup(resize_keyboard=True)

cancel_menu = ReplyKeyboardBuilder()
cancel_menu.button(text="Bekor qilish") 
cancel_menu = cancel_menu.as_markup(resize_keyboard=True)