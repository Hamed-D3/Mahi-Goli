from django import template

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