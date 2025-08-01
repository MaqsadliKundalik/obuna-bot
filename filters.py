from aiogram.types import Message
from aiogram.filters import Filter
from config import ADMINS
from models import User

class IsAdmin(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in ADMINS
    
class IsNotAdmin(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id not in ADMINS
    
class IsNewUser(Filter):
    async def __call__(self, message: Message):
        return not await User.get_or_none(telegram_id=message.from_user.id)