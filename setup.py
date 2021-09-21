from setuptools import setup

setup(
    name='mkdocs-expose-page-metadata',
    version='0.0.1',
    description='This plug-in exposing all pages metadata in a single path!',
    keywords='mkdocs metadata',
    url='https://github.com/herberton/mkdocs-expose-page-metadata',
    author='Herberton Candido Souza',
    author_email='herberton@gmail.com',
    license='Apache-2.0',
    python_requires='>=3',
    packages=['mkdocs_expose_page_metadata'],
    install_requires=[
        'mkdocs>=1.1.2'
    ],
    entry_points={
        'mkdocs.plugins': [
            'mkdocs-expose-page-metadata = mkdocs_expose_page_metadata.plugin:ExposePageMetadataPlugin',
        ]
    }
)