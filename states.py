from aiogram.fsm.state import State, StatesGroup

class SubscribeUserState(StatesGroup):
    send_check = State()

class AdminSendState(StatesGroup):
    msg = State()