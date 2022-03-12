from dataclasses import replace
from django import template

register = template.Library()


@register.simple_tag
def url_replace(request,field,value):
    #GETパラメーターを一部置き換える
    url_dict = request.GET.copy()
    #url_dict: <QueryDict: {'club': [''], 'department': ['']}>
    #URL_dict: club=&department=&page=2の形に変換している
    # {% url_replace request 'page' page_obj.previous_page_number %} page5.htmlでの実行部分
    print(f'url_dict: {url_dict}')
    url_dict[field] = value
    print(f'URL_dict: {url_dict}')
    print(f'URL_encode: {url_dict.urlencode()}')
    return url_dict.urlencode()