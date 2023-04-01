import urwid


def has_digits(password):
    return any(element.isdigit() for element in password)


def has_letters(password):
    return any(element.isalpha() for element in password)


def has_upper_letters(password):
    return any(element.isupper() for element in password)


def has_lower_letters(password):
    return any(element.islower() for element in password)


def has_symbols(password):
    return any(not (element.isdigit() or element.isalpha())
               for element in password)


def is_very_long(password):
    return len(password) > 12


def score_count(edit, new_edit_text):
    score = 0
    for check in checks:
        if check(new_edit_text):
            score += 2
    reply.set_text(f"Рейтинг вашего пароля: {score}")


checks = [
    has_digits,
    has_upper_letters,
    has_letters,
    has_symbols,
    is_very_long,
    has_lower_letters
]

ask = urwid.Edit('Введите пароль: ', mask='*')
reply = urwid.Text("")
menu = urwid.Pile([ask, reply])
menu = urwid.Filler(menu, valign='top')
urwid.connect_signal(ask, 'change', score_count)
urwid.MainLoop(menu).run()
