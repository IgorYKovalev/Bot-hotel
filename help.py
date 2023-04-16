from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def help_keyboard() -> ReplyKeyboardMarkup:
    """
    Создаёт клавиатуру с основными командами бота
    :return: keyboard
    :rtype: ReplyKeyboardMarkup
    """

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    lowprice = KeyboardButton('/lowprice')
    highprice = KeyboardButton('/highprice')
    bestdeal = KeyboardButton('/bestdeal')
    history = KeyboardButton('/history')
    favorites = KeyboardButton('/favorites')
    help_button = KeyboardButton('/help')

    keyboard.row(lowprice, highprice)
    keyboard.row(favorites, bestdeal)
    keyboard.row(history,  help_button)

    return keyboard