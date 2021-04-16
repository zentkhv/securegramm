import config  # скрипт с конфигурацией бота
import logging  # библиотека для вывода логов в консоль
import keyboards  # скрипт со всеми клавиатурами
# import asyncio

from aiogram import Bot, Dispatcher, executor, types  # элементы библиотеки для работы с ботом
from sqlighter import SQLighter  # класс для работы с бд sql

# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# инициализируем соединение с БД
db = SQLighter('main.db')


# Вызываемые функции

# Управление подпиской
async def manager_subscribe(message):
    await bot.send_message(message.from_user.id, 'Что хочешь сделать?',
                           reply_markup=keyboards.get_manager_subscribe_keyboard())


# Обновление номера телефона
async def phone_number_update(message):
    await bot.send_message(message.from_user.id, 'Мы сохранили твой номер для связи, спасибо!')


# Команда старт
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    # добавляем пользователя в таблицу user, если его там еще нет
    if not db.subscriber_exists(message.from_user.id):
        db.add_subscriber(message.from_user.id, message.from_user.username, True)

    await message.answer("Привет! Я бот клуба 4MAFIA.\nИспользуй меню, чтобы общаться со мной!",
                         reply_markup=keyboards.get_main_keyboard())

    db.add_history_log(message.from_user.id, message.from_user.username, message.text)


# Собитие нажатие кнопки подписки
@dp.callback_query_handler(lambda c: c.data == 'button_subscribe')
async def process_callback_button_subscribe(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    if not db.subscriber_exists(callback_query.from_user.id):
        # если юзера нет в базе, добавляем его
        db.add_subscriber(callback_query.from_user.id, callback_query.from_user.username, True)
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_subscription(callback_query.from_user.id, True)

    db.add_history_log(callback_query.from_user.id, callback_query.from_user.username, "Подписаться")  # логирование
    await bot.send_message(callback_query.from_user.id, 'Вы подписались на рассылку 📬')


# Собитие нажатие кнопки отписки
@dp.callback_query_handler(lambda c: c.data == 'button_unsubscribe')
async def process_callback_button_unsubscribe(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    if not db.subscriber_exists(callback_query.from_user.id):
        # если юзера нет в базе, добавляем его с неактивной подпиской (запоминаем)
        db.add_subscriber(callback_query.from_user.id, False)
        await bot.send_message(callback_query.from_user.id, 'Вы итак не подписаны 📪')
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_subscription(callback_query.from_user.id, False)
        await bot.send_message(callback_query.from_user.id, 'Вы отписаны от рассылки 📪')
    db.add_history_log(callback_query.from_user.id, callback_query.from_user.username, "Отписаться")


# Обработка прочих сообщений
@dp.message_handler(content_types=['contact'])
async def get_contact(message: types.Message):
    await bot.send_message(message.from_user.id, message.contact["phone_number"])


# Обработка прочих сообщений
@dp.message_handler()
async def echo_message(message: types.Message):
    if message.text == '📫 Управление подпиской':
        await manager_subscribe(message)
    elif message.text == '☎️Поделиться номером':
        await phone_number_update(message)
    else:
        await bot.send_message(message.from_user.id, 'Я не знаю что ответить...\nЛучше воспользуйся меню')

    db.add_history_log(message.from_user.id, message.from_user.username, message.text)  # логирование


# Запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)