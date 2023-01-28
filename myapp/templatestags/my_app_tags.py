from django import template
import random
from string import ascii_lowercase, digits, ascii_uppercase

register = template.Library()


@register.simple_tag()
def randomnum():
    number = random.randint(1, 9999)
    return number

@register.simple_tag()
def randomslug():
    letters_and_digits = ascii_lowercase + digits
    tyre = '-'
    res = ''.join(random.choices(letters_and_digits, k=4))
    res += ''.join(tyre)
    res += random.choice(ascii_uppercase)
    res += ''.join(random.choices(letters_and_digits, k=6))
    return res
