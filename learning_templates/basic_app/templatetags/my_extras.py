from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "agr" from the string!
    :param value:
    :param arg:
    :return:
    """
    return value.replace(arg, '')


# register.filter('cut', cut)
