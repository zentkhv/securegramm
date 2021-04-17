import sqlite3
from time import strftime


class SQLighter:

    # Подключаемся к БД и сохраняем курсор соединения
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    # Получаем всех активных подписчиков бота
    def get_subscriptions(self, status=True):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `user` WHERE `status` = ?", (status,)).fetchall()

    # Проверяем, есть ли уже юзер в базе
    def subscriber_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `user` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))

    # Добавляем нового подписчика
    def add_subscriber(self, user_id, user_name, status=True):
        with self.connection:
            now_datetime = strftime("%d.%m.%y %H:%M:%S")
            return self.cursor.execute("INSERT INTO `user` (`user_id`, user_name, `status`, `sub_date`,`last_change`) "
                                       "VALUES(?,?,?,?,?)",
                                       (user_id, user_name, status, now_datetime, now_datetime))

    # Обновляем статус подписки пользователя
    def update_subscription(self, user_id, status):
        with self.connection:
            now_datetime = strftime("%d.%m.%y %H:%M:%S")
            return self.cursor.execute("UPDATE `user` SET `status` = ?, `last_change` = ? WHERE `user_id` = ?",
                                       (status, now_datetime, user_id))

    # Обновляем номер телефона
    def update_phone_number(self, user_id, phone_number):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `phone_number` = ? WHERE `user_id` = ?",
                                       (phone_number, user_id))

    # Обновляем никнейм
    def update_nickname(self, user_id, nickname):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `nickname` = ? WHERE `user_id` = ?",
                                       (nickname, user_id))

    # Добавляем лог переписки с пользователем
    def add_history_log(self, user_id, user_name, text):

        with self.connection:
            now_datetime = strftime("%d.%m.%y %H:%M:%S")
            return self.cursor.execute("INSERT INTO `history` (`user_id`, user_name, `datetime`,`message_text`) "
                                       "VALUES(?,?,?,?)",
                                       (user_id, user_name, now_datetime, text))

    # Закрываем соединение с БД
    def close(self):
        self.connection.close()
