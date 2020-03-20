from django import template

register = template.Library()

@register.filter(name="cutcut")
def cut(value, arg):
    return value.replace(arg, '')
