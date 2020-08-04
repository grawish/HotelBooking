from django import template

register = template.Library()


@register.filter()
def to_int(value):
    return int(value)


def to_str(value):
    return str(value)
