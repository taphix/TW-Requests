from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_kb(
        *buttons: str,
        placeholder: str | None = None,
        request_contact: int | None = None,
        request_location: int | None = None,
        sizes: tuple[int] = (2,)
        ):
    keyboard = ReplyKeyboardBuilder()
    for idx, text in enumerate(buttons):
        if request_contact and request_contact == idx + 1:
            keyboard.add(KeyboardButton(text=text, request_contact=True))
        elif request_location and request_location == idx + 1:
            keyboard.add(KeyboardButton(text=text, request_location=True))
        else:
            keyboard.add(KeyboardButton(text=text))
    return keyboard.adjust(*sizes).as_markup(
        resize_keyboard=True, input_field_placeholder=placeholder
    )


START_KB = get_kb(
        'Зарегистрироваться.',
        'Добавить комментарий.',
        'Посмотреть всех пользователей.',
        'Посмотреть все комментарии.',
        placeholder='Что вас интересует?',
        sizes=(1,)
)

ADD_KB = get_kb(
    'Выйти без сохранения'
)
