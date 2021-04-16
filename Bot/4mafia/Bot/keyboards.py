from aiogram import Bot, Dispatcher, executor, types


# Основная обычная клавиатура
def get_main_keyboard():
    # клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_sub = types.KeyboardButton('📫 Управление подпиской')
    item_phone = types.KeyboardButton('☎️Оставить номер', request_contact=True)
    markup.add(item_sub, item_phone)
    return markup


# Inline клавиатура управления подпиской
def get_manager_subscribe_keyboard():
    inline_button_subscribe = types.InlineKeyboardButton('📬 Подписаться', callback_data='button_subscribe')
    inline_button_unsubscribe = types.InlineKeyboardButton('📪 Отписаться', callback_data='button_unsubscribe')
    return types.InlineKeyboardMarkup().add(inline_button_subscribe, inline_button_unsubscribe)

