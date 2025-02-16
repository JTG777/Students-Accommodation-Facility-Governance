from django import template


register=template.Library()


@register.filter
def multiply(room_fee,duration):
    try:
        return room_fee*duration
    except (TypeError,ValueError):
        return 0
    

@register.filter
def divide(food_charge,duration):
    try:

        return food_charge/duration
    
    except (TypeError,ValueError):
        return 0