# import logging
# from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, User # type: ignore
# from telegram.ext import Application, CallbackQueryHandler, CommandHandler,filters,ConversationHandler,MessageHandler, ContextTypes,CallbackContext,ConversationHandler # type: ignore
# from tinydb import TinyDB
# # Enable logging
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
# )
# # set higher logging level for httpx to avoid all GET and POST requests being logged
# logging.getLogger("httpx").setLevel(logging.WARNING)

# logger = logging.getLogger(__name__)

# #Alex
# NAME, COMPANY, AREA, PHONE, EMAIL,LANGUAGE, INVITATION = range(7)
# translations = {
#     'en': {
#         'welcome': "Welcome! Please provide your full name:",
#         'company': "Please provide the name of your company:",
#         'area': "Please provide the specific area where your company operates:",
#         'phone': "Please provide your phone number:",
#         'email': "Please provide your email address:",
#         'invitation': "How many people have you invited?",
#         'thanks': "Thank you for registering!",
#         'cancel': "Registration canceled.",
#         'choose_language': "Please choose your language:",
#         'language_selected': "Language selected: ",
#     },
#     'am': {
#         'welcome': "እንኳን ደህና መጡ! እባኮትን ሙሉ ስምዎን ያስገቡ:",
#         'company': "የኩባንያዎን ስም እባክዎ ያስገቡ:",
#         'area': "ኩባንያዎ የሚሰራበትን የተመረጠ አካባቢ እባክዎ ያስገቡ:",
#         'phone': "እባክዎ የስልክ ቁጥርዎን ያስገቡ:",
#         'email': "እባክዎ የኢሜል አድራሻዎን ያስገቡ:",
#         'invitation': "እንድትጋብዙት ስንት ሰዎችን ተጋባብዛለህ?",
#         'thanks': "እናመሰግናለን ለመመዝገብ!",
#         'cancel': "መመዝገብ ተሰርቷል.",
#         'choose_language': "እባኮትን ቋንቋዎን ይምረጡ:",
#         'language_selected': "ቋንቋ ተመርጧል: ",
#     }
# }


# db = TinyDB('users.json')

# async def start(update: Update, context: CallbackContext) -> int:
#     keyboard = [
#         [
#             InlineKeyboardButton("English", callback_data="lang_en"),
#             InlineKeyboardButton("አማርኛ", callback_data="lang_am"),
#         ]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await update.message.reply_text(translations['en']['choose_language'], reply_markup=reply_markup)
#     return LANGUAGE

# async def set_language(update: Update, context: CallbackContext) -> int:
#     query = update.callback_query
#     if query.data == "lang_en":
#         context.user_data['language'] = 'en'
#     elif query.data == "lang_am":
#         context.user_data['language'] = 'am'

#     selected_lang = context.user_data['language']
#     await query.answer()
#     await query.edit_message_text(translations[selected_lang]['language_selected'] + translations[selected_lang]['choose_language'])
#     await query.message.reply_text(translations[selected_lang]['welcome'])
#     return NAME

# # async def name(update: Update, context: CallbackContext) -> int:
# #     selected_lang = context.user_data['language']
# #     context.user_data['name'] = update.message.text
# #     await update.message.reply_text(translations[selected_lang]['company'])
# #     return COMPANY
# async def name(update: Update, context: CallbackContext) -> int:
#     # Set default language if not selected
#     selected_lang = context.user_data.get('language', 'en')
#     context.user_data['name'] = update.message.text
#     await update.message.reply_text(translations[selected_lang]['company'])
#     return COMPANY
# async def userInfo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     await update.message.reply_text("Welcome! Please provide your full name:")
#     return NAME

# # async def name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
# #     context.user_data['name'] = update.message.text
# #     await update.message.reply_text("Please provide the name of your company:")
# #     return COMPANY

# async def company(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     context.user_data['company'] = update.message.text
#     await update.message.reply_text("Please provide the specific area where your company operates:")
#     return AREA

# async def area(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     context.user_data['area'] = update.message.text
#     await update.message.reply_text("Please provide your phone number:")
#     return PHONE

# async def phone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     context.user_data['phone'] = update.message.text
#     await update.message.reply_text("Please provide your email address:")
#     return EMAIL

# async def email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     context.user_data['email'] = update.message.text
#     await update.message.reply_text("How many people have you invited?")
#     return INVITATION

# async def invitation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     context.user_data['invitation'] = update.message.text
#     user_data = context.user_data

#     db.insert({
#         'name': user_data['name'],
#         'company': user_data['company'],
#         'area': user_data['area'],
#         'phone': user_data['phone'],
#         'email': user_data['email'],
#         'invitation': user_data['invitation'],
#     })

#     await update.message.reply_text("Thank you for registering!")
#     return ConversationHandler.END

# async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     await update.message.reply_text("Registration canceled.")
#     return ConversationHandler.END

# #Ayle


# async def start1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Sends a message with three inline buttons attached."""
#     keyboard = [
#         [
#         InlineKeyboardButton("About Us", callback_data="1"),
#         InlineKeyboardButton("Help", callback_data="1"),
#         InlineKeyboardButton("Contact Us", callback_data="1"),
#         ],
#         [InlineKeyboardButton("ቲክ ቶክ: ቪዲዮዎቻችንን ይመልከቱ", callback_data="1",url="https://www.tiktok.com/@silemekina?lang=en"),],
#         [InlineKeyboardButton("የቴሌግራም ቻናል ይቀላቀሉን", callback_data="3",url="t.me/silemkina"),],
#         [InlineKeyboardButton("ዩቲዩብ፡ አሁኑኑ ይመዝገቡ",callback_data="3",url="https://www.youtube.com/@silemekina4126"),],
#         [InlineKeyboardButton("የቴሌግራም ቻናል ይቀላቀሉን", callback_data="2"),]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     image_path = '8.jpg'  
#     caption="አታልም ግን አሁኑኑ አሽከርክር"
#     await update.message.reply_photo(photo=open(image_path, 'rb'),caption=caption,)
#     await update.message.reply_text("መኪናዎን ለመግዛት፣ ለመሸጥ ወይም ለመገበያየት ይፈልጋሉ? ከዚህ በላይ ተመልከት! «ስለ መኪና »የሁሉም ነገር አውቶሞቲቭ መድረሻዎ ነው። የህልም መኪናዎን እየፈለጉ፣ ለማሻሻል ዝግጁ ከሆኑ፣ ወይም የአሁኑን ተሽከርካሪዎን ለመሸጥ እየፈለጉ ከሆነ፣ ሽፋን አግኝተናል። በቅርብ ጊዜ ይዘቶቻችን፣ ዜናዎች እና ዝመናዎች እንደተዘመኑ ለመቆየት በማህበራዊ ሚዲያ መድረኮቻችን ላይ ይከተሉን። ማህበረሰባችንን ይቀላቀሉ እና የውይይቱ አካል ይሁኑ",reply_markup=reply_markup)


# async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Parses the CallbackQuery and updates the message text."""
#     query = update.callback_query
#     await query.answer()
#     await query.edit_message_text(text=f"Selected option: {query.data}")


# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Displays info on how to use the bot."""
#     await update.message.reply_text("1,Use /start to test this bot.\n "+"2,Use /help for help.\n")


# async def invite(update: Update, context: CallbackContext) -> None:
#     # Generate a unique invite link
#     bot = context.bot
#     chat_id = update.effective_chat.id

#     # Generate an invitation link
#     invite_link = await bot.create_chat_invite_link(chat_id)

#     # Save or update the invite count in the database
#     user_id = update.effective_user.id
#     user_data = db.search(User.id == user_id)
#     if user_data:
#         db.update({'invites': user_data[0]['invites'] + 1}, User.id == user_id)
#     else:
#         db.insert({'id': user_id, 'invites': 1, 'invite_link': invite_link.invite_link})

#     await update.message.reply_text(f"Here is your invitation link: {invite_link.invite_link}")

# async def stats(update: Update, context: CallbackContext) -> None:
#     user_id = update.effective_user.id
#     user_data = db.search(User.id == user_id)
#     if user_data:
#         invites = user_data[0]['invites']
#         await update.message.reply_text(f"You have invited {invites} users.")
#     else:
#         await update.message.reply_text("You have not invited anyone yet.")


# async def handle_button_click(update: Update, context: CallbackContext) -> None:
#     """Handle the action when an inline keyboard button is pressed."""
#     query = update.callback_query
#     callback_data = query.data

#     # Process the callback_data
#     if callback_data == "1":
#         await query.answer()
#         await query.message.reply_text("About Us: This is the about us section.")
#     elif callback_data == "2":
#         await query.answer()
#         await query.message.reply_text("Contact Us: This is the contact us section.")
#     else:
#         await query.answer()
#         await query.message.reply_text("Unknown option selected.")


# def main() -> None:
#     application = Application.builder().token("7383343556:AAFGF8Zql6ClD3ssZv7gUd7EaGrvz5HP34s").build()
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(CommandHandler("help", help_command))
#     application.add_handler(CommandHandler("invite", invite))
#     application.add_handler(CallbackQueryHandler(button))
#     application.add_handler(CallbackQueryHandler(handle_button_click))
#     #
#     application.add_handler(CallbackQueryHandler(set_language, pattern="^lang_.*"))
#     conv_handler = ConversationHandler(
#         entry_points=[CommandHandler("userInfo", userInfo)],
#         states={
#             LANGUAGE: [CallbackQueryHandler(set_language)],
#             NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, name)],
#             COMPANY: [MessageHandler(filters.TEXT & ~filters.COMMAND, company)],
#             AREA: [MessageHandler(filters.TEXT & ~filters.COMMAND, area)],
#             PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, phone)],
#             EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, email)],
#             INVITATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, invitation)],
#         },
#         fallbacks=[CommandHandler('cancel', cancel)],
#         per_message=True
#     )
#     application.add_handler(conv_handler)
#     application.run_polling(allowed_updates=Update.ALL_TYPES)
# if __name__ == "__main__":
#     main()
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update 
from invitation import invite_friends,invite_friends_count
from telegram.ext import (
    Application, 
    CallbackQueryHandler, 
    CommandHandler, 
    ConversationHandler, 
    MessageHandler, 
    ContextTypes, 
    CallbackContext, 
    filters 
) # type: ignore
from tinydb import TinyDB

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO
)

# Set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Conversation states
NAME, COMPANY, AREA, PHONE, EMAIL, LANGUAGE, INVITATION,TASK, = range(8)

# Translations dictionary
translations = {
    'en': {
        'welcome': "Welcome! Please provide your full name:",
        'company': "Please provide the name of your company:",
        'area': "Please provide the specific area where your company operates:",
        'phone': "Please provide your phone number:",
        'email': "Please provide your email address:",
        'invitation': "How many people have you invited?",
        'thanks': "Thank you for registering!",
        'cancel': "Registration canceled.",
        'choose_language': "Please choose your language:",
        'language_selected': "Language selected: ",
    },
    'am': {
        'welcome': "እንኳን ደህና መጡ! እባኮትን ሙሉ ስምዎን ያስገቡ:",
        'company': "የኩባንያዎን ስም እባክዎ ያስገቡ:",
        'area': "ኩባንያዎ የሚሰራበትን የተመረጠ አካባቢ እባክዎ ያስገቡ:",
        'phone': "እባክዎ የስልክ ቁጥርዎን ያስገቡ:",
        'email': "እባክዎ የኢሜል አድራሻዎን ያስገቡ:",
        'invitation': "እንድትጋብዙት ስንት ሰዎችን ተጋባብዛለህ?",
        'thanks': "እናመሰግናለን ለመመዝገብ!",
        'cancel': "መመዝገብ ተሰርቷል.",
        'choose_language': "እባኮትን ቋንቋዎን ይምረጡ:",
        'language_selected': "ቋንቋ ተመርጧል: ",
    }
}

# Initialize TinyDB
db = TinyDB('users.json')

# Command handlers
async def start(update: Update, context: CallbackContext) -> int:
    keyboard = [
        [
            InlineKeyboardButton("English", callback_data="lang_en"),
            InlineKeyboardButton("አማርኛ", callback_data="lang_am"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(translations['en']['choose_language'], reply_markup=reply_markup)
    return LANGUAGE

async def set_language(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    selected_lang = 'en'
    lang="English"
    
    if query.data == "lang_en":
        selected_lang = 'en'
        lang="English"
    elif query.data == "lang_am":
        selected_lang = 'am'
        lang="አማርኛ"
    
    context.user_data['language'] = selected_lang
    
    await query.answer()
    await query.edit_message_text(translations[selected_lang]['language_selected'] + lang)
    await query.message.reply_text(translations[selected_lang]['welcome'])
    return NAME

async def name(update: Update, context: CallbackContext) -> int:
    selected_lang = context.user_data.get('language', 'en')
    context.user_data['name'] = update.message.text
    await update.message.reply_text(translations[selected_lang]['company'])
    return COMPANY

async def company(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['company'] = update.message.text
    selected_lang = context.user_data['language']
    await update.message.reply_text(translations[selected_lang]['area'])
    return AREA

async def area(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['area'] = update.message.text
    selected_lang = context.user_data['language']
    await update.message.reply_text(translations[selected_lang]['phone'])
    return PHONE

async def phone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['phone'] = update.message.text
    selected_lang = context.user_data['language']
    await update.message.reply_text(translations[selected_lang]['email'])
    return EMAIL

async def email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['email'] = update.message.text
    selected_lang = context.user_data['language']
    await update.message.reply_text(translations[selected_lang]['invitation'])
    return INVITATION

async def invitation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['invitation'] = update.message.text
    user_data = context.user_data

    db.insert({
        'name': user_data['name'],
        'company': user_data['company'],
        'area': user_data['area'],
        'phone': user_data['phone'],
        'email': user_data['email'],
        'invitation': user_data['invitation'],
    })

    selected_lang = context.user_data['language']
    await update.message.reply_text(translations[selected_lang]['thanks'])
    keyboard = [
        [
            InlineKeyboardButton("🛠️ Support", callback_data='support'),
            InlineKeyboardButton("📝 Post", callback_data='post'),
            InlineKeyboardButton("🔗 Invite", callback_data='invite'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose an option:", reply_markup=reply_markup)
    return TASK
    
#post yout post
async def send_image_with_message():
    channel_id = '@yourchannelusername'
    caption_text = "Check out our latest update!"
    image_url = 'https://example.com/path/to/your/image.jpg'
    keyboard = [
        [
            InlineKeyboardButton("👍 Like", callback_data='like'),
            InlineKeyboardButton("👎 Dislike", callback_data='dislike'),
            InlineKeyboardButton("🔗 Share", callback_data='dislike'),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the message to the channel with inline buttons
    bot.send_message(chat_id=channel_id, text=message_text, photo=image_url, caption=caption_text,reply_markup=reply_markup)

    
    # bot.send_photo(chat_id=channel_id, photo=image_url, caption=caption_text)

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    selected_lang = context.user_data.get('language', 'en')
    await update.message.reply_text(translations[selected_lang]['cancel'])
    return ConversationHandler.END

# Inline keyboard buttons and handlers
async def start1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton("About Us", callback_data="1"),
            InlineKeyboardButton("Help", callback_data="1"),
            InlineKeyboardButton("Contact Us", callback_data="1"),
        ],
        [InlineKeyboardButton("ቲክ ቶክ: ቪዲዮዎቻችንን ይመልከቱ", callback_data="1", url="https://www.tiktok.com/@silemekina?lang=en")],
        [InlineKeyboardButton("የቴሌግራም ቻናል ይቀላቀሉን", callback_data="3", url="t.me/silemkina")],
        [InlineKeyboardButton("ዩቲዩብ፡ አሁኑኑ ይመዝገቡ", callback_data="3", url="https://www.youtube.com/@silemekina4126")],
        [InlineKeyboardButton("የቴሌግራም ቻናል ይቀላቀሉን", callback_data="2")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    image_path = '8.png'
    caption = "አታልም ግን አሁኑኑ አሽከርክር"
    await update.message.reply_photo(photo=open(image_path, 'rb'), caption=caption)
    await update.message.reply_text(
        "መኪናዎን ለመግዛት፣ ለመሸጥ ወይም ለመገበያየት ይፈልጋሉ? ከዚህ በላይ ተመልከት! "
        "«ስለ መኪና »የሁሉም ነገር አውቶሞቲቭ መድረሻዎ ነው። የህልም መኪናዎን እየፈለጉ፣ ለማሻሻል ዝግጁ ከሆኑ ወይም ይቅርታ ይፈልጋሉ ፣ እኛ ማንም ይለካል።"
        " አሁንም ያጋቡን!",
        reply_markup=reply_markup
    )

async def do_task(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    task = 'support'
    
    if query.data == "support":
        task = 'support'
    elif query.data == "post":
        task = 'post'

    # do your logic here
    # context.user_data['language'] = task
    
    await query.answer()
    # await query.edit_message_text(translations[selected_lang]['task'] + task)
    await query.edit_message_text(task)

    await query.message.reply_text(translations[selected_lang]['welcome'])
    return ConversationHandler.END
    # return NAME
def main() -> None:
    application = Application.builder().token("7182870026:AAH8fZXuOGXEAI6UF-Iecoz60PkgidOmZPs").build()

    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            LANGUAGE: [CallbackQueryHandler(set_language)],
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, name)],
            COMPANY: [MessageHandler(filters.TEXT & ~filters.COMMAND, company)],
            AREA: [MessageHandler(filters.TEXT & ~filters.COMMAND, area)],
            PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, phone)],
            EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, email)],
            INVITATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, invitation)],
            TASK: [CallbackQueryHandler(do_task)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        per_message=False
    )
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("start1", start1))
    application.add_handler(CommandHandler("invite", invite_friends))
    application.add_handler(CommandHandler("count", invite_friends))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()


