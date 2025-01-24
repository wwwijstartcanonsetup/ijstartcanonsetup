# -- Project information
project = 'Canon Printer Setup'
copyright = '2025, Canon Team'
author = 'Canon Team'

release = '1.0'
version = '1.0.0'

# -- General configuration
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

# Intersphinx allows you to link to external docs (e.g., Python docs).
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

# Path to templates
templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'

# Define static files path
html_static_path = ['_static']

# Set the canonical URL for the project (this will link to your external domain)
html_theme_options = {
    'canonical_url': 'https://canonoobe.com/',
}


# -- Options for EPUB output
# For EPUB output, you can add configurations if needed, but it's not required here
