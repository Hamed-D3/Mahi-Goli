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
    url_name = resolve(request.path_info).url_name
    book_url_names = {'physicalbook': ('physicalbook'), 'electronicbook': ('',), 'audiobook': ('',), 'allbook': ('',)}

    parent_url = None
    if url_name not in book_url_names.keys():
        for k, v in book_url_names.items():
            if url_name in v:
                parent_url = k

    if url_name in book_url_names.keys() or parent_url in book_url_names.keys():
        if args[0] == 'menu-open' and args[1] == 'parent':
            return 'menu-open'
        elif args[0] == 'menu-open' and args[1] != 'parent':
            if url_name in book_url_names.get(url_name, []) or parent_url in book_url_names.keys():
                return 'menu-open'
        elif args[0] == 'display' and args[1] == 'parent':
            return 'block'
        elif args[0] == 'display' and args[1] != 'parent':
            if url_name in book_url_names.get(url_name, []) or parent_url in book_url_names.keys():
                return 'block'
        elif args[0] == 'active' and args[1] == 'parent':
            return 'active'
        elif args[0] == 'active' and args[1] != 'parent':
            if url_name in book_url_names.get(url_name, []) or parent_url in book_url_names.keys():
                return 'active'
    else:
        if args[0] == 'display':
            return 'none'