from django.template.base import Library, Node

register = Library()

@register.filter
def range(number):
	return range(number)