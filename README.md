# mkdocs-expose-page-metadata

[![PyPI](https://img.shields.io/pypi/v/mkdocs-expose-page-metadata)](https://pypi.org/project/mkdocs-expose-page-metadata/)
[![PyPI - License](https://img.shields.io/pypi/l/mkdocs-expose-page-metadata)](LICENSE)

This plug-in exposing all pages metadata in a single path!

## How to use?

Just follow the steps:

1. Add dependency on your `requirements.txt`:

    ```
    ...
    mkdocs-expose-page-metadata==0.0.1
    
    ```

2. Enable plug-in on your `mkdocs.yml`:

    ```yaml
        ...

        plugins:
            - mkdocs-expose-page-metadata
            ...
    ```
 
3. Create any metadata in your markdown, for example on `lorem-ipsum.md`:

    ```markdown
    ---
    title: Some metadata title
    tags:
        - First Tag
        - Second Tag
    other-metadata: bla
    ---

    # Lorem Ipsum
    ...
    ```

4. Build and run you project, for exemple, with `mkdocs serve` command;

5. Check all page metadata in a single endpoint: `/metadata/metadata.json`:

    ```json
    [
        {
            "meta" : {
                "title": "Some metadata title",
                "tags": [
                    "First Tag",
                    "Second Tag"
                ],
                "other-metadata": "bla"
            },
            "title": "Lorem Ipsum",
            "url": "/lorem-ipsum"
        }
    ]
    ```