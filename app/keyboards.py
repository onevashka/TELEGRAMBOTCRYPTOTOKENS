from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                        InlineKeyboardMarkup, InlineKeyboardButton )

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = "Portfolio"),KeyboardButton(text = "Buy")],
    [KeyboardButton(text = "Manu")],
    
],  
                            resize_keyboard=True,
                            input_field_placeholder="сделай свой выбор")

settings = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text = f"BTC", url = "https://cryptorank.io/price/bitcoin" ), InlineKeyboardButton(text = f"ETH", url = "https://cryptorank.io/price/ethereum" )],
                                                [InlineKeyboardButton(text = "BNB", url = "https://cryptorank.io/price/bnb"), InlineKeyboardButton(text = "SOL", url = "https://cryptorank.io/price/solana")]])