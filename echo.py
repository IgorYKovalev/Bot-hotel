from loader import bot
from telebot.types import Message


@bot.message_handler(content_types=['text'], state=None)
def echo(message: Message) -> None:
    """
    Функция реакции на сообщение, не являющееся командой.
    :param message: Объект сообщения.
    :type message: Message
    :return: None
    """

    if message.text.lower().startswith('прив'):
        bot.send_message(message.chat.id,
                         "Привет! Я найду для тебя лучшие отели на сайте hotels.com (кроме России)! "
                         "Чтобы узнать, что я умею, введи /help")
    else:
        bot.send_message(message.chat.id,
                         "Я могу помочь найти лучшие отели!\n"
                         "Посмотри тут /help, чтобы узнать больше!")
