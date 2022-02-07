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
    book_url_names = {'physicalbook': ('physicalbook', 'physicalbook_create',), 
                    'electronicbook': ('electronicbook', 'electronicbook_create',), 
                    'audiobook': ('audiobook', 'audiobook_create',), 
                    'allbook': ('', 'allbook'),
                    'category': ('category', 'category_create'),
                    'author': ('author', 'author_create'),
                    'translator': ('translator', 'translator_create'),
                    'teller': ('teller', 'teller_create'),
                    'publisher': ('publisher', 'publisher_create')}

    url_name_books = {'physicalbook': ('physicalbook', 'physicalbook_create',), 
                    'electronicbook': ('electronicbook', 'electronicbook_create',), 
                    'audiobook': ('audiobook', 'audiobook_create',), 
                    'allbook': ('', 'allbook')}

    sub_url = [sub_url for sub_url in url_name_books.values()]
    all_urlname_book = []
    for url_tuple in sub_url:
        for url in url_tuple:
            all_urlname_book.append(url)

    parent_url = None
    if url_name not in book_url_names.keys():
        for k, v in book_url_names.items():
            if url_name in v:
                parent_url = k

    if url_name in book_url_names.keys() or parent_url in book_url_names.keys():
        if args[0] == 'menu-open' and args[1] == 'parent':
            if (url_name in url_name_books.get(url_name, []) or url_name in all_urlname_book) or (parent_url in url_name_books.keys() or parent_url in all_urlname_book):
                return 'menu-open'
        elif args[0] == 'menu-open' and args[1] != 'parent':
            if (url_name in book_url_names.get(url_name, []) and args[1] == url_name) or (parent_url in book_url_names.keys() and args[1] == parent_url):
                return 'menu-open'
            else:
                return ''
        elif args[0] == 'display' and args[1] == 'parent':
            if (url_name in url_name_books.get(url_name, []) or url_name in all_urlname_book) or (parent_url in url_name_books.keys() or parent_url in all_urlname_book):
                return 'block'
        elif args[0] == 'display' and args[1] != 'parent':
            if (url_name in book_url_names.get(url_name, []) and args[1] == url_name) or (parent_url in book_url_names.keys() and args[1] == parent_url):
                return 'block'
            else:
                return ''
        elif args[0] == 'active' and args[1] == 'parent':
            if (url_name in url_name_books.get(url_name, []) or url_name in all_urlname_book) or (parent_url in url_name_books.keys() or parent_url in all_urlname_book):
                return 'active'
        elif args[0] == 'active' and args[1] != 'parent':
            if (url_name in book_url_names.get(url_name, []) and args[1] == url_name) or (parent_url in book_url_names.keys() and args[1] == parent_url):
                return 'active'
            else:
                return ''
    else:
        if args[0] == 'display':
            return 'none'