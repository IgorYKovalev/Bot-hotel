from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def hotel_details_keyboard(hotel_id: int,
                           photo_shown: bool,
                           in_favorites: bool
                           ) -> InlineKeyboardMarkup:
    """
    Создаёт клавиатуру для действий с отелем.
    :param hotel_id: id отеля
    :type hotel_id: int
    :param photo_shown: флаг - показаны ли фото
    :type photo_shown: bool
    :param in_favorites: Флаг - добавлен ли в избранное
    :type in_favorites: bool
    :return: keyboard
    :rtype: InlineKeyboardMarkup
    """

    hotel_link = f'https://www.hotels.com/h{hotel_id}.Hotel-Information'

    keyboard = InlineKeyboardMarkup()

    booking = InlineKeyboardButton(text='Забронировать', url=hotel_link)
    show_photo = InlineKeyboardButton(text='Показать фото', callback_data='PHOTO|' + str(hotel_id))
    add_to_favorite = InlineKeyboardButton(text='Добавить в избранное', callback_data='ADD_FAVORITE|' + str(hotel_id))
    delete_favorite = InlineKeyboardButton(text='Убрать из избранного', callback_data='DELETE_FAVORITE|' + str(hotel_id))
    hide = InlineKeyboardButton(text='Скрыть', callback_data='HIDE')

    keyboard.add(booking)
    if not photo_shown:
        keyboard.add(show_photo)
    if not in_favorites:
        keyboard.add(add_to_favorite)
    else:
        keyboard.add(delete_favorite)
    keyboard.add(hide)

    return keyboard