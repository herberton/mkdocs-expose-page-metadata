from mkdocs_expose_page_metadata.metadata import Metadata

class MetadataPageEntry:

    @property
    def title(self) -> str:
        return self._TITLE

    @property
    def url(self) -> str:
        return self._URL

    @property
    def meta(self) -> Metadata:
        return self._META

    def __init__(self, title: str, url: str, meta: dict=None, annotations: list[str] = []):
        self._TITLE = title
        self._URL = url
        self._META = Metadata(content=meta, annotations=annotations)

    def to_dict(self):
        return {
            'title': self.title,
            'url': self.url,
            'meta': self.meta.content
        }
