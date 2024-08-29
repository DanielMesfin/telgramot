from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler
from tinydb import TinyDB

NAME, COMPANY, AREA, PHONE, EMAIL, INVITATION = range(6)

db = TinyDB('users.json')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Welcome! Please provide your full name:")
    return NAME

async def name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['name'] = update.message.text
    await update.message.reply_text("Please provide the name of your company:")
    return COMPANY

async def company(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['company'] = update.message.text
    await update.message.reply_text("Please provide the specific area where your company operates:")
    return AREA

async def area(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['area'] = update.message.text
    await update.message.reply_text("Please provide your phone number:")
    return PHONE

async def phone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['phone'] = update.message.text
    await update.message.reply_text("Please provide your email address:")
    return EMAIL

async def email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['email'] = update.message.text
    await update.message.reply_text("How many people have you invited?")
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

    await update.message.reply_text("Thank you for registering!")
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Registration canceled.")
    return ConversationHandler.END

def main() -> None:
    application = Application.builder().token("7383343556:AAFGF8Zql6ClD3ssZv7gUd7EaGrvz5HP34s").build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, name)],
            COMPANY: [MessageHandler(filters.TEXT & ~filters.COMMAND, company)],
            AREA: [MessageHandler(filters.TEXT & ~filters.COMMAND, area)],
            PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, phone)],
            EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, email)],
            INVITATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, invitation)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    application.add_handler(conv_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
