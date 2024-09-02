import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from invitation import invite_friends,invite_friends_count
from telegram import Bot
from tinydb import TinyDB,Query
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    ContextTypes,
    CallbackContext,
    filters
)

# db = TinyDB('users.json')
STAKEHOLDER_TELEGRAM_ID = '979896547'
TELEGRAM_TOKEN='7182870026:AAH8fZXuOGXEAI6UF-Iecoz60PkgidOmZPs'
bot = Bot(token=TELEGRAM_TOKEN)
db = TinyDB('db.json')
users_table = db.table('users')
# In-memory invite links for simplicity. In production, store them in the database.
invite_links = {}
# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
# Set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)
# Conversation states
NAME, COMPANY, AREA, PHONE, EMAIL, LANGUAGE,TOBEMEMBER, INVITATION,TASK, = range(9)
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
        'task':"Complete your tasks, contribute to our community, and start earning money today! Together, we can grow stronger while you achieve your financial goals."

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
         'task': "ተግባሮችዎን ያጠናቅቁ ፣ ለማህበረሰባችን ያዋጡ እና ዛሬ ገንዘብ ማግኘት ይጀምሩ! አንድ ላይ፣ የፋይናንስ ግቦችዎን በሚያሳኩበት ጊዜ የበለጠ ጠንካራ ማደግ እንችላለን።",
        'language_selected': "ቋንቋ ተመርጧል: ",
    }
}

async def start(update: Update, context: CallbackContext) -> int:
    user_first_name = update.message.from_user.first_name
    keyboard = [
        [
            InlineKeyboardButton("About Us", callback_data="1"),
            InlineKeyboardButton("Help", callback_data="1"),
            InlineKeyboardButton("Contact Us", callback_data="1"),
            ],
            [InlineKeyboardButton(text='Visit our YouTube Channel', url='https://www.youtube.com/@gyeontechnology')],
            [InlineKeyboardButton("ቲክ ቶክ: ቪዲዮዎቻችንን ይመልከቱ",  url="https://www.tiktok.com/@silemekina?lang=en")],
            [InlineKeyboardButton("የቴሌግራም ቻናል ይቀላቀሉን", url="t.me/silemkina")],
            [InlineKeyboardButton("ዩቲዩብ፡ አሁኑኑ ይመዝገቡ",  url="https://www.youtube.com/@silemekina4126")],
            [InlineKeyboardButton("አሁኑኑ ይመዝገቡ", callback_data="tobemember")],
            ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    image_path = 'images/agent.png'
    caption=f"🎉🎉 ሰላም {user_first_name}፣ እና እንኳን ደህና መጣህ! እዚህ በማግኘታችን በጣም ደስ ብሎናል።\n \n🎉🎉 እየገዙም፣ እየሸጡም፣ወይም እያሰሱም፣ ትክክለኛው ቦታ ላይ ነዎት።\n\n እርዳታ ይፈልጋሉ? ብቻ ይጠይቁ፣ እና የመንገዱን እያንዳንዱን እርምጃ ልንረዳዎ እዚህ መጥተናል።\n\n🎉🎉 ተሞክሮዎን ለስላሳ እና አስደሳች እናድርገው!"
    await update.message.reply_photo(photo=open(image_path, 'rb'), caption=caption)
    await update.message.reply_text(text="Click the button below to visit our social media", reply_markup=reply_markup)
    return TOBEMEMBER
async def to_be_member(update: Update, context: CallbackContext) -> int:
    user_first_name = update.message.from_user.first_name
    text=f"🎉🎉 ሰላም {user_first_name}፣ እና እንኳን ደህና መጣህ! እዚህ በማግኘታችን በጣም ደስ ብሎናል። እየገዙም፣ እየሸጡም፣ ወይም እያሰሱም፣ ትክክለኛው ቦታ ላይ ነዎት። እርዳታ ይፈልጋሉ? ብቻ ይጠይቁ፣ እና የመንገዱን እያንዳንዱን እርምጃ ልንረዳዎ እዚህ መጥተናል። ተሞክሮዎን ለስላሳ እና አስደሳች እናድርገው!"
    keyboard = [
        [
            InlineKeyboardButton("English", callback_data="lang_en"),
            InlineKeyboardButton("አማርኛ", callback_data="lang_am"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, reply_markup=reply_markup)
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
# email
async def email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['email'] = update.message.text
    selected_lang = context.user_data['language']
    await update.message.reply_text(translations[selected_lang]['invitation'])
    return INVITATION
# user registrations
async def register(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
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
    await update.message.reply_text(translations[selected_lang]['thanks'], reply_markup=reply_markup)
    return TASK
# postin mensage
async def post_image_with_message():
    channel_id = '@yourchannelusername'
    caption_text = "Check out our latest update!"
    image_url = '8.png'
    keyboard = [
        [
            InlineKeyboardButton("👍 Like", callback_data='like'),
            InlineKeyboardButton("👎 Dislike", callback_data='dislike'),
            InlineKeyboardButton("🔗 Share", callback_data='dislike'),
        ],
    ]
    message_text="these is the product "
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the message to the channel with inline buttons
    bot.send_message(chat_id=channel_id, text=message_text, photo=image_url, caption=caption_text,reply_markup=reply_markup)
# cancel options
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    selected_lang = context.user_data.get('language', 'en')
    await update.message.reply_text(translations[selected_lang]['cancel'])
    return ConversationHandler.END
# Task managment for the system
async def do_task(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    task = 'support'

    if query.data == "support":
        task = 'support'
    elif query.data == "post":
        task = 'post'

    await query.answer()
    # await query.edit_message_text(translations[selected_lang]['task'] + task)
    await query.edit_message_text(task)
    # await query.message.reply_text(translations[selected_lang]['welcome'])
    return ConversationHandler.END
# Function to fetch and forward user data
async def forward_user_data(update: Update, context: ContextTypes.DEFAULT_TYPE)->int:
    telegram_id = str(update.message.from_user.id)
    User = Query()
    users = db.all()
    if users:
        user_info = f"All User Information:\n\n"
        for user in users:
            user_info += "------------------\n"
            for key, value in user.items():
                user_info += f"{key}: {value}\n"
            user_info += "------------------\n"
        # Send the formatted data to the stakeholder
        await bot.send_message(chat_id='979896547', text=user_info)
    else:
        await bot.send_message(chat_id='979896547', text="User not found.")


# Function to add a new user to the database
def add_user(user_id, username, parent_id=None):
    if not users_table.contains(Query().user_id == user_id):
        users_table.insert({
            'user_id': user_id,
            'username': username,
            'parent_id': parent_id,
            'invites': 0,
            'transactions': []
        })

# Start command to welcome the user
async def start12(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    username = update.message.from_user.username

    # Check if user already exists and add if not
    if not users_table.contains(Query().user_id == user_id):
        add_user(user_id, username)

    await update.message.reply_text(
        f"Welcome {username}! Use /invite12 to generate an invitation link."
    )

# Generate an invitation link for the user
async def invite12(update: Update, context: CallbackContext) -> None:
    bot = Bot(token=TELEGRAM_TOKEN)
    updates = bot.get_updates()
    # print("chanl id")
    # print(updates.message.chat.id)
    # for update in updates:
    #     print("chanl id")
    #     print(update.message.chat.id)
    user_id = update.message.from_user.id
    chat_id = "@free_promotion_agent_bot"# Replace with your public group/channel ID
    bot = context.bot

    # Ensure the user has initiated with /start
    if not users_table.contains(Query().user_id == user_id):
        await update.message.reply_text("Please use /start first.")
        return

    # Generate a one-time use invite link
    invite_link = await bot.create_chat_invite_link(chat_id=chat_id, member_limit=1)
    invite_links[invite_link.invite_link] = user_id  # Store the creator of the invite link

    await update.message.reply_text(f"Here is your invite link: {invite_link.invite_link}")

# Handle new members joining through invite links
async def new_member(update: Update, context: CallbackContext) -> None:
    for member in update.message.new_chat_members:
        invite_link = update.message.text  # Assuming this contains the invite link

        if invite_link in invite_links:
            parent_id = invite_links[invite_link]
            user_id = member.id
            username = member.username

            # Add the new user with the inviter's ID as parent_id
            add_user(user_id, username, parent_id)

            # Increment the inviter's invite count
            users_table.update({'invites': Query().invites + 1}, Query().user_id == parent_id)

            await update.message.reply_text(
                f"{member.username} has joined using your invite link! Total invites: {users_table.get(Query().user_id == parent_id)['invites']}"
            )

# Fetch children (invited users) for a specific parent
async def children(update: Update, context: CallbackContext) -> None:
    parent_id = update.message.from_user.id
    children = users_table.search(Query().parent_id == parent_id)
    
    if children:
        response = "Here are your invited users:\n"
        response += "\n".join([f"Username: {child['username']}" for child in children])
    else:
        response = "You haven't invited anyone yet."

    await update.message.reply_text(response)

def main() -> None:
    
    application = Application.builder().token("7182870026:AAH8fZXuOGXEAI6UF-Iecoz60PkgidOmZPs").build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            TOBEMEMBER: [CallbackQueryHandler(set_language)],
            LANGUAGE: [CallbackQueryHandler(set_language)],
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, name)],
            COMPANY: [MessageHandler(filters.TEXT & ~filters.COMMAND, company)],
            AREA: [MessageHandler(filters.TEXT & ~filters.COMMAND, area)],
            PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, phone)],
            EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, email)],
            INVITATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, register)],
            TASK: [CallbackQueryHandler(do_task)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        per_message=False
    )
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("invite", invite_friends))
    application.add_handler(CommandHandler("start12", start12))

    application.add_handler(CommandHandler("invite12", invite12))
    application.add_handler(CommandHandler("user", forward_user_data))
    application.add_handler(CommandHandler("post", post_image_with_message ))
    application.add_handler(CommandHandler("user", forward_user_data))
    # application.add_handler(CommandHandler("new", invite_new_user))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()


