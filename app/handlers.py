
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from coins_data import get_price
import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"HELLO, I'm your bot that will find the price of t", reply_markup=kb.settings)

@router.message(Command("help"))
async def get_help(message: Message):
    await message.answer()
    
@router.message(Command("menu"))

@router.message(F.text)
async def get_price_messange(message: Message):
    price =  await get_price(message.text)
    if price is not None:
        await message.reply(price)
    else:
        await message.reply("Please, enter corect token")