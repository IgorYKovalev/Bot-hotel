from loader import bot
from telebot.types import Message
from keyboards.reply_keyboards.help import help_keyboard


@bot.message_handler(commands=['help'])
def help_command(message: Message) -> None:
    """
    Функция справка (команда /help)
    :param message: Объект сообщения.
    :type message: Message
    :return: None
    """

    bot.send_message(message.chat.id, "Вот, что я умею:\n"
                                      "\n"
                                      "/lowprice: Топ самых дешевых отелей по выбранному направлению\n"
                                      "/highprice: Топ самых дорогих отелей по выбранному направлению\n"
                                      "/bestdeal: Топ предложений по вашему запросу\n(близость к центру/цена)\n"
                                      "/history: История поиска\n"
                                      "/favorites: Избранные отели\n"
                                      "/help: Повторный вывод справки", reply_markup=help_keyboard())