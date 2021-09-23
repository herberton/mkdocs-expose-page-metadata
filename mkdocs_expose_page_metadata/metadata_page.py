import os

from mkdocs import utils
from mkdocs.structure.pages import Page
from mkdocs_expose_page_metadata.metadata_page_entry import MetadataPageEntry
from mkdocs_expose_page_metadata.helpers import to_json
from mkdocs_expose_page_metadata.metadata_parser import MetadataParser

class MetadataPage:

    # CONSTANTS

    PATH = "metadata"
    NAME = "metadata.json"
    ENCODE = "utf-8"

    # CONSTRUCTOR

    def __init__(self, path: str, name: str, encode: str):
        self._PATH = path if path else self.PATH
        self._NAME = name if name else self.NAME
        self._ENCODE = encode if encode else self.ENCODE
        self._CONTENT = list[MetadataPageEntry]()

    # METHODS

    def append_content_from(self, page: Page):

        if page.meta:
            entry = MetadataPageEntry(title=page.title, location=page.url, meta=page.meta)
            self._CONTENT.append(entry)

        parser = MetadataParser(page)

        for entry in parser.entries:
            if (not entry.location):
                raise Exception(f"Location not found for subtitle \"{entry.title}\" on page \"{page.title}\"")
            self._CONTENT.append(entry)

    def save(self):
        endpoint = os.path.join(self._PATH, self._NAME)
        content = self.__str__()
        utils.write_file(content.encode(self._ENCODE), endpoint)
    
    def __repr__(self) -> str:
        return to_json([entry.to_dict() for entry in self._CONTENT])
