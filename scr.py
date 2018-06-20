# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot("605943675:AAHbUDKkHFfyhIffuhF3m_AuGA8h8mQtz2Q")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе

    bot.send_message(message.chat.id, "Пошёл ты на хер,КОЗЁЛ!!!")
    photo = open('kozel.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo)
if __name__ == '__main__':
     bot.polling(none_stop=True)
