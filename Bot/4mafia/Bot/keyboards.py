from aiogram import Bot, Dispatcher, executor, types


# Основная обычная клавиатура
def get_main_keyboard():
    # клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_settings = types.KeyboardButton('🛠 Настройки')
    markup.add(item_settings)
    return markup


# Клавиатура настроек
def get_settings_keyboard():
    # клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_sub = types.KeyboardButton('📫 Рассылка')
    item_phone = types.KeyboardButton('☎️Оставить номер', request_contact=True)
    item_nickname = types.KeyboardButton('📜️ Записать ник')
    item_back = types.KeyboardButton('🏠 Главное меню')
    markup.add(item_sub, item_phone)
    markup.add(item_nickname)
    markup.add(item_back)
    return markup


# Inline клавиатура управления подпиской
def get_manager_subscribe_keyboard():
    inline_button_subscribe = types.InlineKeyboardButton('📬 Включить', callback_data='button_subscribe')
    inline_button_unsubscribe = types.InlineKeyboardButton('📪 Выключить', callback_data='button_unsubscribe')
    return types.InlineKeyboardMarkup().add(inline_button_subscribe, inline_button_unsubscribe)
