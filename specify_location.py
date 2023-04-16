from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def specify_location_keyboard(locations_dict: dict) -> InlineKeyboardMarkup:
    """
    Создаёт клавиатуру для выбора конкретной локации из списка
    :return: keyboard
    :rtype: InlineKeyboardMarkup
    """

    keyboard = InlineKeyboardMarkup(row_width=1)

    for key in locations_dict.keys():
        keyboard.add(InlineKeyboardButton(text=key, callback_data=locations_dict[key]))

    try_again = InlineKeyboardButton(text='Начать сначала', callback_data='TRY_AGAIN')
    stop_search = InlineKeyboardButton(text='Закончить поиск', callback_data='CANCEL')

    keyboard.add(try_again)
    keyboard.add(stop_search)

    return keyboard