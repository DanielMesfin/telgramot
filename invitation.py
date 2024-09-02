from telegram import Update
from telegram.ext import CallbackContext
from tinydb import TinyDB, Query

db = TinyDB('db.json')

def generate_invite_link(user_id):
    return f"https://t.me/free_promotion_agent_bot?start={user_id}"

async def invite_friends(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    invite_link = generate_invite_link(user_id)
    
    # Store user data if new
    if not db.search(Query().user_id == user_id):
        db.insert({'user_id': user_id, 'invites': 0, 'rewards': []})
    
    # Handle invite parameter if present
    if context.args:
        inviter_id = context.args[0]
        inviter_data = db.search(Query().user_id == inviter_id)
        if inviter_data:
            # Update the number of invites
            db.update({'invites': inviter_data[0]['invites'] + 1}, Query().user_id == inviter_id)
            # Check if a reward should be given
            new_invite_count = inviter_data[0]['invites'] + 1
            if new_invite_count % 5 == 0:  # For example, give a reward every 5 invites
                db.update({'rewards': inviter_data[0]['rewards'] + ['RewardX']}, Query().user_id == inviter_id)
                await context.bot.send_message(chat_id=inviter_id, text="Congratulations! You earned a reward.")
    await update.message.reply_text(f"Invite others using this link: {invite_link}")

async def invite_friends_count(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    user_data = db.search(Query().user_id == user_id)
    if user_data:
        await update.message.reply_text(f"You have invited {user_data[0]['invites']} users.")
    else:
        await update.message.reply_text("You haven't invited anyone yet.")

