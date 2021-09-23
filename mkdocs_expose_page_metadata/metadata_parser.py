import re

from mkdocs.structure.pages import Page
from mkdocs_expose_page_metadata.helpers import create_parser_from, get_subtitle_url_from
from mkdocs_expose_page_metadata.metadata_page_entry import MetadataPageEntry

class MetadataParser:

    _PAGE_MARKDOWN_REGEX = re.compile(r"(#+\s*.*\s*(\[.*\]:<.*>\s*\(.*\)\s*)+)")
    _PAGE_SUBTITLE_REGEX = re.compile(r"(#+\s*.*)")
    _PAGE_ANNOTATIONS_REGEX = re.compile(r"(\[.*\]:<.*>\s*\(.*\)\s*)")

    @property
    def entries(self) -> list[MetadataPageEntry]:
        return self._ENTRIES

    def __init__(self, page: Page):

        self._ENTRIES = []

        parser = create_parser_from(page)

        matches = self._PAGE_MARKDOWN_REGEX.finditer(page.markdown)
        for match in matches:

            text = match.group(0)

            subtitle = self._PAGE_SUBTITLE_REGEX.search(text).group(0)
            url = get_subtitle_url_from(page=page, parser=parser, subtitle=subtitle)
            annotations = [annotation.group(0).strip() for annotation in self._PAGE_ANNOTATIONS_REGEX.finditer(text)]

            self._ENTRIES.append(MetadataPageEntry(title=subtitle, url=url, annotations=annotations))

