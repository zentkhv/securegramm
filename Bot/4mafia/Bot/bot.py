import config
import logging
import asyncio

from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types

# задаем уровень логов
from sqlighter import SQLighter

logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# инициализируем соединение с БД
db = SQLighter('maindb.db')


# Команда активации подписки
@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    if not db.subscriber_exists(message.from_user.id):
        # если юзера нет в базе, добавляем его
        db.add_subscriber(message.from_user.id, message.from_user.username, True)
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_subscription(message.from_user.id, True)

    await message.answer(
        "Вы успешно подписались на рассылку!")


# Команда отписки
@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
    if not db.subscriber_exists(message.from_user.id):
        # если юзера нет в базе, добавляем его с неактивной подпиской (запоминаем)
        db.add_subscriber(message.from_user.id, False)
        await message.answer("Вы итак не подписаны.")
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_subscription(message.from_user.id, False)
        await message.answer("Вы успешно отписаны от рассылки.")


# запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
