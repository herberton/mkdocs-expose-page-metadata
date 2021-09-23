from mkdocs_expose_page_metadata.metadata import Metadata

class MetadataPageEntry:

    # PROPERTIES

    @property
    def title(self) -> str:
        return self._TITLE

    @property
    def location(self) -> str:
        return self._LOCATION

    @property
    def meta(self) -> Metadata:
        return self._META

    # CONSTRUCTOR

    def __init__(self, title: str, location: str, meta: dict=None, annotations: list[str] = []):
        self._TITLE = title
        self._LOCATION = location
        self._META = Metadata(content=meta, annotations=annotations)

    # METHODS

    def to_dict(self):
        return {
            'title': self.title,
            'location': self.location,
            'meta': self.meta.content
        }
