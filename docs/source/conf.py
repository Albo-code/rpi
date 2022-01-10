# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('./../../'))
sys.path.insert(1, os.path.abspath('./../../camera'))


# -- Project information -----------------------------------------------------

project = 'rpi'
copyright = '2021, Albo-code'
author = 'Albo-code'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.linkcode'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# If given, this must be the name of an image file (path relative to the
# configuration directory) that is the favicon of the docs, or URL that points
# an image file for the favicon. Modern browsers use this as the icon for tabs,
# windows and bookmarks. It should be a Windows-style icon file (.ico), which
# is 16x16 or 32x32 pixels large. Default: None.
html_favicon = 'raspberrypi_favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# -- Options autodoc

# This value contains a list of modules to be mocked up. This is useful when
# some external dependencies are not met at build time and break the building
# process. You may only specify the root package of the dependencies themselves
# and omit the sub-modules:
autodoc_mock_imports = ['picamera']

# -- sphinx.ext.linkcode
# See https://www.sphinx-doc.org/en/master/usage/extensions/linkcode.html

LINKCODE_REPO_URL = 'https://github.com/Albo-code/rpi/tree'
# Update following to "main" when initial branch merged
LINKCODE_REPO_BRANCH = 'InitialCamDev'

def linkcode_resolve(domain, info):
    if domain != 'py':
        return None
    if not info['module']:
        return None
    filename = info['module'].replace('.', '/')
    print(f"domin={domain}, info={info}")
    return f"{LINKCODE_REPO_URL}/{LINKCODE_REPO_BRANCH}/{filename}.py"
