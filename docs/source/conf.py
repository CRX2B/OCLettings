import os
import sys
import django

# Configuration file for the Sphinx documentation builder.
sys.path.insert(0, os.path.abspath('../../'))

# Désactiver Sentry explicitement pour la génération de la documentation
os.environ["SENTRY_DSN"] = ""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
django.setup()

# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Orange County Lettings'
copyright = '2025, Thomas Jeanne'
author = 'Thomas Jeanne'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
