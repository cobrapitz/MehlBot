# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__name__), ".."))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = "MehlBot"
copyright = "2023, Cobrapitz"
author = "Cobrapitz"
version = release = "1.1.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

source_suffix = ".rst"

master_doc = "index"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx.ext.githubpages",
    "sphinx_rtd_theme",
    "sphinx.ext.autosummary",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "en"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"  # 'alabaster'
html_static_path = ["_static"]

autosummary_generate = True
