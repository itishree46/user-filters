from django import template

register=template.Library()

def swapping(value):
    return value.swapcase()

register.filter('swap',swapping)  #register.filter('name of filter',function name)

def counting(value,sub):
    c=0
    for i in range(len(value)):
        if value[i:i+len(sub)]==sub:
            c+=1
    return c

register.filter('count',counting)
    