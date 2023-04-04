import random
import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "YOUR_BOT_TOKEN"

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Emoji sets
gay_emojis = ['🧔‍♀️', '👰🏻‍♂️', '👯‍♂️', '👬', '👨‍❤️‍👨', '💑', '👨‍❤️‍💋‍👨', '🌈', '🤼‍♂️', '💝', '🏳️‍🌈', '🫂', '👥']
vegetable_emojis = ['🍆', '🌶', '🥒', '🥕', '🌽', '🥖', '🍌', '🍾']

def roll_emojis():
    selected_set = random.choices([gay_emojis, vegetable_emojis], weights=[5, 15])[0]
    if random.random() <= 0.0001:
        return ['🌈'] * 3
    elif random.random() <= 0.1:
        emoji = random.choice(selected_set)
        return [emoji, emoji, emoji]
    else:
        return random.sample(selected_set, 3)

def roll(update: Update, context: CallbackContext):
    emoji_list = roll_emojis()
    rolled_emojis = ''.join(emoji_list)
    message_id = update.message.message_id
    chat_id = update.message.chat_id

    # Send the rolled emoji result first
    context.bot.send_message(chat_id=chat_id, text=rolled_emojis, reply_to_message_id=message_id)

    if rolled_emojis == '🌈🌈🌈':
        user_first_name = update.message.from_user.first_name
        reply_text = f"🎉ПОЗДРОВЛЕНИЯ!!! 🎉{user_first_name} ВЫ СУПИРПИДОР! 🎉"
        context.bot.send_message(chat_id=chat_id, text=reply_text, reply_to_message_id=message_id)
    elif len(set(emoji_list)) == 1:
        user_first_name = update.message.from_user.first_name
        winning_message = f"ПОЗДРОВЛЕНИЕ {user_first_name}! ВЫ ПИДОР {rolled_emojis}"
        context.bot.send_message(chat_id=chat_id, text=winning_message, reply_to_message_id=message_id)



def main():
    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("roll", roll))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
