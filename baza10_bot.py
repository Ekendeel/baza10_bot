import telebot
import random

TOKEN = '8009135131:AAHu7SPlXj25mebzzCCyWH7vOwOloUt_3B4'
bot = telebot.TeleBot(TOKEN)

# Загружаем и подготавливаем данные
with open('БАЗА 10.txt', 'r', encoding='utf-8') as file:
    content = file.read().strip().split('\n\n\n')

# Сохраняем уже отправленные сообщения для каждого пользователя
sent_messages = {}

# Главное меню с кнопкой BAZA
def main_menu():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('🔥 BAZA')
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    sent_messages[message.chat.id] = set()
    bot.send_message(
        message.chat.id, 
        "Нажми кнопку «🔥 BAZA», чтобы получить контент.", 
        reply_markup=main_menu()
    )

@bot.message_handler(func=lambda message: message.text == '🔥 BAZA')
def send_random_content(message):
    chat_id = message.chat.id

    if chat_id not in sent_messages:
        sent_messages[chat_id] = set()

    available_messages = list(set(content) - sent_messages[chat_id])

    if not available_messages:
        sent_messages[chat_id] = set()
        available_messages = content.copy()
        bot.send_message(chat_id, "🔄 Все сообщения отправлены! Начинаю заново.")

    selected_message = random.choice(available_messages)
    sent_messages[chat_id].add(selected_message)

    bot.send_message(chat_id, selected_message)

# Запуск бота
bot.infinity_polling()
