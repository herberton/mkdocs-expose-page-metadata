# mkdocs-expose-page-metadata

[![PyPI](https://img.shields.io/pypi/v/mkdocs-expose-page-metadata)](https://pypi.org/project/mkdocs-expose-page-metadata/)
[![PyPI - License](https://img.shields.io/pypi/l/mkdocs-expose-page-metadata)](LICENSE)

This plug-in exposing all pages metadata in a single path!

## How to use?

Just follow the steps:

1. Add dependency on your `requirements.txt`:

    ```
    ...
    mkdocs-expose-page-metadata==1.1.6
    
    ```

2. Enable plug-in on your `mkdocs.yml`:

    ```yaml
    ...

    plugins:
        - mkdocs-expose-page-metadata
    ...
    ```

    1. Is possible to set these config parameters:
    
        |**Parameter**|**Type**|**Description**|**Default Value**|
        |-|-|-|-|
        |**metadata_page_path**|`str`|Metadata page path|`metadata`|
        |**metadata_page_name**|`str`|Metadata page name|`metadata.json`|
        |**metadata_page_encode**|`str`|Metadata page encode|`utf-8`|

3. Create any metadata in your markdown, for example on `lorem-ipsum.md`:

    ```markdown
    ---
    title: Some metadata title
    tags:
        - First Tag
        - Second Tag
    other-metadata: bla
    ---

    # Lorem Ipsum 1
    
    Some text 1
    
    # Lorem Ipsum 2
    
    [meta]:<test> (Some text)
    [meta]:<first-middle-tags> (First middle tag value 1)
    [meta]:<first-middle-tags> (First middle tag value 2)
    
    Some text 2
    
    ## Lorem Ipsum 2-1
    
    [second-middle-tags]:<> (Second middle tag value 1)
    [second-middle-tags]:<> (Second middle tag value 2)
    
    Some text 2-1
    
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
            "location": "/lorem-ipsum"
        },
        {
            "meta" : {
                "test": "Some text",
                "first-middle-tags": [
                    "First middle tag value 1",
                    "First middle tag value 2"
                ]
            },
            "title": "Lorem Ipsum 2",
            "location": "/lorem-ipsum/#lorem-ipsum-2"
        },
        {
            "meta" : {
                "second-middle-tags": [
                    "Second middle tag value 1",
                    "Second middle tag value 2"
                ]
            },
            "title": "Lorem Ipsum 2-1",
            "location": "/lorem-ipsum/#lorem-ipsum-2-1"
        }
    ]
    ```