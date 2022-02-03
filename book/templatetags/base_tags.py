from django import template
from django.urls import resolve

register = template.Library()

@register.inclusion_tag('book/partials/sidebar_item.html')
def sidebar_item(request, link_name, content, icon_classes):
    return {
        'request': request,
        'link_name': link_name,
        'link': f'book:{link_name}',
        'content': content,
        'icon_classes': icon_classes
    }


@register.simple_tag
def active_book_item(request, *args):
    book_url_names = ('physicalbook', 'electronicbook', 'audiobook', 'allbook')
    if resolve(request.path_info).url_name in book_url_names:
        if args[0] == 'menu-open':
            return 'menu-open'
        elif args[0] == 'active':
            return 'active'
        elif args[0] == 'display':
            return 'block'
    else:
        if args[0] == 'display':
            return 'none'