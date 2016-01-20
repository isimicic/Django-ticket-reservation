from django import template

register = template.Library()


@register.filter
def isIn(value, arg):
    """ Filter for Django template check if arg is in value list"""
    return arg in value
