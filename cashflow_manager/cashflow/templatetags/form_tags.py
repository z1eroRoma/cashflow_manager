from django import template
from django.forms.fields import BoundField

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    if isinstance(field, BoundField):
        return field.as_widget(attrs={"class": css_class})
    return field

@register.filter(name='attr')
def attr(field, attrs_str):
    if isinstance(field, BoundField):
        attrs = {}
        for attr in attrs_str.split(','):
            key, value = attr.split(':')
            attrs[key.strip()] = value.strip()
        return field.as_widget(attrs=attrs)
    return field
