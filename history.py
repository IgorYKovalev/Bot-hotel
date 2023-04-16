from telebot import types


def history_keyboard(history_record_id: int) -> types.InlineKeyboardMarkup:
    """
    Клавиатура для записи истории
    :param history_record_id: id записи истории в базе данных
    :type history_record_id: int
    """
    keyboard = types.InlineKeyboardMarkup()
    delete = types.InlineKeyboardButton(text='Удалить запись', callback_data='DELETE|' + str(history_record_id))
    clear_history =types.InlineKeyboardButton(text='Очистить историю', callback_data='CLEAR')

    keyboard.add(delete)
    keyboard.add(clear_history)

    return keyboard

