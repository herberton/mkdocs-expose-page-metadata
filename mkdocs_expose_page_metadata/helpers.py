import json

from mkdocs.contrib.search.search_index import ContentParser
from mkdocs.structure.pages import Page

def find_toc_by_id(toc, _id):
    for toc_item in toc:
        if toc_item.id == _id:
            return toc_item
        toc_item_r = find_toc_by_id(toc_item.children, _id)
        if toc_item_r is not None:
            return toc_item_r

def get_location_from(page: Page, parser: ContentParser, subtitle: str):

    _subtitle = string_remove(text=subtitle, old="#", strip=True)

    for section in parser.data:
        toc_item = find_toc_by_id(page.toc, section.id)
        toc_item_title = string_remove(text=toc_item.title if toc_item else "", old="#", strip=True)
        if toc_item_title == _subtitle:
            return page.url + toc_item.url

    return None

def string_remove(text: str, old: str, count: int=-1, strip: bool=False):
    return string_replace(text=text, old=old, count=count, strip=strip)

def string_replace(text: str, old: str, new:str="", count: int=-1, strip: bool=False):
    if not text:
        return text
    result = text.replace(old, new if new else "", count if count else -1)
    return result.strip() if strip else result

def create_parser_from(page: Page):
    parser = ContentParser()
    parser.feed(page.content)
    parser.close()
    return parser

def to_json(object):
    return json.dumps(object, default=lambda o: o.__dict__, separators=(',', ':'), sort_keys=True)

def dict_merge(base: dict={}, new: dict={}) -> dict:
    _new = new if new else {}
    _base = base if base else {}
    for key in _new.keys():
        _base[key] = dict_merge_value(_base, key, _new[key])
    return _base

def dict_merge_value(base: dict={}, key: str=None, value=None):
    _base = base if base else {}
    if key and key in _base:
        _value = _base[key] if isinstance(_base[key],list) else [_base[key]]
        _value.append(value)
        return _value
    else:
        return value
