from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def location_type_keyboard() -> InlineKeyboardMarkup:
    """
    Создаёт клавиатуру для выбора типа локации
    :return: keyboard
    :rtype: InlineKeyboardMarkup
    """

    keyboard = InlineKeyboardMarkup()
    city_group = InlineKeyboardButton(text='Введите название города', callback_data='CITY')
    stop_search = InlineKeyboardButton(text='Закончить поиск', callback_data='CANCEL')

    keyboard.add(city_group)
    keyboard.add(stop_search)

    return keyboard
