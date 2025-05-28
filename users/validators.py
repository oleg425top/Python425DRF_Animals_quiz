import re
from django.core.exceptions import ValidationError


class PasswordValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg_pattern = re.compile(r'^[A-Za-z0-9]+$')
        temp_value = dict(value).get(self.field)
        if not bool(reg_pattern.match(temp_value)):
            raise ValidationError('Ошибка: Пароль должен содержать только латинские буквы и цифры')
