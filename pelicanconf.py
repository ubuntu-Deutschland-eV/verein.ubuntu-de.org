#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = 'ubuntu'
SITENAME = 'ubuntu Deutschland e.V.'
SITEURL = ''

MENUITEMS = (
                ('News', 'news/'),
            )

DEFAULT_LANG = 'de'
TIMEZONE = 'Europe/Berlin'
DEFAULT_DATE_FORMAT = '%a, %-d. %B %Y'
DEFAULT_DATE = (1970, 1, 1, 0, 1, 1)
CURRENTYEAR = date.today().year

SUMMARY_MAX_LENGTH = 50

PATH = 'content'
IGNORE_FILES = ['.#*', 'files']
STATIC_PATHS = ['files']
THEME = 'themes/verein'

JINJA_ENVIRONMENT = {'trim_blocks': True,
                     'lstrip_blocks': True,
                     'extensions': ['jinja2.ext.ExprStmtExtension',]}

## Plugins ##

LOCALE = 'de_DE.utf-8' # for open_graph

PLUGIN_PATHS = ['plugins']
PLUGINS = [
            'pelican-page-order',
            'assets',
#            'pelican-open_graph',
            'sitemap',
          ]

ASSET_SOURCE_PATHS = [
    'vendor',
]

SITEMAP = {
    'format': 'xml',
    }

# only one Atome Feed with all news
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# no pagination
DEFAULT_PAGINATION = False

## URL-settings ##

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

INDEX_SAVE_AS = 'news/index.html'

ARTICLE_URL = ARTICLE_SAVE_AS = ''

# author, categories and tags should not been generated
AUTHORS_SAVE_AS = AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = CATEGORIES_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
TAG_URL = TAG_SAVE_AS = ''
TAGS_URL = TAGS_SAVE_AS = ''

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
