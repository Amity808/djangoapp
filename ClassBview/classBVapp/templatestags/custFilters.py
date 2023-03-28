from django import template

register= template.Library()

@register.filter(name='mylower')
def custLower(value):
    result=value[:3].lower()
    return result
