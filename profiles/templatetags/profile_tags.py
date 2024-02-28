from django import template
from ..models import Profile

register = template.Library()

@register.filter
def get_current_address(obj:Profile):
    return obj.address.get(current_address = True)
