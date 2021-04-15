import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


# команда start
@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("/start")

    markup.add(item1, item2)
    # sticker
    sti = open('stickers/AnimatedSticker.tgs', 'rb')

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
    bot.send_sticker(message.chat.id, sti)


# обработка
@bot.message_handler(content_types=['text'])
def main_def(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        else:
            bot.send_message(message.chat.id, 'Я пока не знаю такой команды :(')


# RUN
bot.polling(none_stop=True)
