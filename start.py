from loader import bot
from telebot.types import Message
from keyboards.reply_keyboards.help import help_keyboard


@bot.message_handler(commands=['start', 'hello-world'])
def greetings(message: Message) -> None:
    """
    Функция-приветствие (команды /start и /hello-world)
    :param message: Объект сообщения.
    :type message: Message
    :return: None
    """

    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}!\n'
                                      f'Я найду для тебя лучшие отели на сайте hotels.com (кроме России)\n'
                                      'Чтобы начать, посмотри тут /help', reply_markup=help_keyboard())
