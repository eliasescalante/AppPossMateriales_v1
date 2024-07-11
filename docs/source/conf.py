# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

# Obtener la ruta absoluta del directorio actual del archivo conf.py
current_dir = os.path.abspath(os.path.dirname(__file__))

# Subir tres niveles en la estructura de directorios
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))

# Agregar la carpeta raíz del proyecto al path de Python
sys.path.insert(0, root_dir)

project = 'proyecto nivel intermedio'
copyright = '2024, elias, imelda, carmen'
author = 'elias, imelda, carmen'
release = '0.01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

