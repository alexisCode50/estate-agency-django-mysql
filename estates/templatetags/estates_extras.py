from django import template

register = template.Library()

def price(value):
	"""Converts a string into all lowercase"""
	return '{:,}'.format(value)

register.filter('price', price)