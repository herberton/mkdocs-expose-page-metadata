
import os

from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
from mkdocs_expose_page_metadata.metadata_page import MetadataPage


class ExposePageMetadataPlugin(BasePlugin):

    # CONSTANTS

    _METADATA_PAGE_PATH_CONFIG = "metadata_page_path"
    _METADATA_PAGE_NAME_CONFIG = "metadata_page_name"
    _METADATA_PAGE_ENCODE_CONFIG = "metadata_page_encode"

    # ATTRIBUTES

    config_scheme = (
        (_METADATA_PAGE_PATH_CONFIG, config_options.Type(str, default=MetadataPage.PATH)),
        (_METADATA_PAGE_NAME_CONFIG, config_options.Type(str, default=MetadataPage.NAME)),
        (_METADATA_PAGE_ENCODE_CONFIG, config_options.Type(str, default=MetadataPage.ENCODE)),
    )

    # EVENTS

    def on_pre_build(self, config):
        self.metadata = MetadataPage(
            path=os.path.join(config['site_dir'], self.config[self._METADATA_PAGE_PATH_CONFIG]),
            name=self.config[self._METADATA_PAGE_NAME_CONFIG],
            encode=self.config[self._METADATA_PAGE_ENCODE_CONFIG]
        )

    def on_page_context(self, context, **kwargs):
        "Metadata Page Creation"
        page = context['page']
        self.metadata.append_content_from(page)

    def on_post_build(self, config, **kwargs):
        "Metadata Page Building"
        self.metadata.save()
