
import os
import json 
from mkdocs.plugins import BasePlugin
from mkdocs import utils

class ExposePageMetadataPlugin(BasePlugin):
    def __init__(self):
        self.path = "metadata"
        self.page = "metadata.json"
        self.metadata = []

    def _add_metadata(self, page):
        if page.meta:
            self.metadata.append({
                'title': page.title,
                'url': page.url,
                'meta': page.meta
            })

    def _build_content(self):
        _metadata = self.metadata if self.metadata else []
        _separators = (',', ':')
        return json.dumps(_metadata, separators=_separators, sort_keys=True)

    def _build_endpoint(self, config):
        _site_dir = config['site_dir']
        _path = os.path.join(_site_dir, self.path)
        return os.path.join(_path, self.page)

    def _save_page(self, page, endpoint):
        utils.write_file(page.encode('utf-8'), endpoint)


    def on_page_context(self, context, **kwargs):
        "Metadata Page Creation"
        self._add_metadata(context['page'])

    def on_post_build(self, config, **kwargs):
        "Metadata Page Building"
        _content = self._build_content()
        _endpoint = self._build_endpoint(config)
        self._save_page(_content, _endpoint)

