from mkdocs_expose_page_metadata.helpers import string_remove, dict_merge, dict_merge_value

class Metadata:

    @property
    def content(self) -> dict:
        return self._CONTENT

    def __init__(self, content: dict=None, annotations: list[str]=[]):
        self._CONTENT = dict_merge(content, self._extract_content_from(annotations))

    def _extract_content_from(self, annotations: list[str]) -> dict:
        content = {}
        for annotation in annotations:
            key, value = self._extract_entry_from(annotation)
            if key:
                content[key] = dict_merge_value(content, key, value)
        return content

    def _extract_entry_from(self, annotation: str) -> (str, str):

        # [meta]:<key> (value)
        if annotation.startswith("[meta]:"):
            _annotation = string_remove(text=annotation, old="[meta]:", count=1, strip=True)
            key = _annotation[1:_annotation.find(">")]
            value = _annotation[_annotation.find(">")+1:].strip()[1:-1]
            return (key, value)

        # [key]:<> (value)
        if annotation.startswith(f"[{annotation[1:annotation.find(']')]}]:<>"):
            key = annotation[1:annotation.find(']')]
            value = annotation[annotation.find('<>')+2:].strip()[1:-1]
            return (key, value)

        print(f'This metadata annotation is invalid: {annotation} ! It will not be displayed in the metadata page!')
        return None
