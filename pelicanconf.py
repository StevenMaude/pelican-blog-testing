#!/usr/bin/env python
# -*- coding: utf-8 -*- #
AUTHOR = 'Steven Maude'
SITENAME = 'stevenmaude.co.uk'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGINS = ['pelican_alias', 'tag_cloud', 'i18n_subsites']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.admonition': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}

THEME = 'theme/pelican-bootstrap3/pelican-bootstrap3'

STATIC_PATHS = ['images']
STATIC_EXCLUDES = ['images/.git']
IGNORE_FILES = ['.#*', 'README.md', '.git']

# Tidy up URLs; remove .html from most of them except index pages.
# Files have .html suffix but GitHub Pages will find page without .html in URL.
# INDEX_SAVE_AS omitted since GitHub needs home page to be index.html
# so can't fix the issue of index pages having .html suffix
ARTICLE_URL = 'posts/{slug}'
ARTICLE_SAVE_AS = ARTICLE_URL + '.html'
ARTICLE_LANG_URL = '{slug}-{lang}'
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL + '.html'

DRAFT_URL = 'drafts/{slug}'
DRAFT_SAVE_AS = DRAFT_URL + '.html'
DRAFT_LANG_URL = 'drafts/{slug}-{lang}'
DRAFT_LANG_SAVE_AS = DRAFT_LANG_URL + '.html'

PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = PAGE_URL + '.html'
PAGE_LANG_URL = 'pages/{slug}-{lang}'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}' + '.html'

CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = CATEGORY_URL + '.html'

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = TAG_URL + '.html'

AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = AUTHOR_URL + '.html'

ARCHIVES_URL = 'archives'
ARCHIVES_SAVE_AS = ARCHIVES_URL + '.html'
AUTHORS_URL = 'authors'
AUTHORS_SAVE_AS = AUTHORS_URL + '.html'
CATEGORIES_URL = 'categories'
CATEGORIES_SAVE_AS = CATEGORIES_URL + '.html'
TAGS_URL = 'tags'
TAGS_SAVE_AS = TAGS_URL + '.html'

# custom pelican-bootstrap3 specific configuration below here
BOOTSTRAP_THEME = 'cosmo-custom'
BOOTSTRAP_NAVBAR_INVERSE = False

BANNER = 'images/extra/banner.jpg'
BANNER_TITLE = "Steven Maude's blog"
BANNER_SUBTITLE = "Words and stuff."

# Pygments
PYGMENTS_STYLE = 'monokai'

# Article info
#SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True

# Navbar
DISPLAY_CATEGORIES_ON_MENU = False
DISABLE_TRANSITIONS = True

# Index page
DISPLAY_ARTICLE_INFO_ON_INDEX = True
USE_PAGER = True

# Sidebar
#DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_MAX_ITEMS = 10
TAG_CLOUD_STEPS = 3
#HIDE_SIDEBAR = True

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

CUSTOM_CSS = 'theme/css/custom.css'

EXTRA_PATH_METADATA = {
    'images/extra/favicon.ico': {'path': 'favicon.ico'},
    'theme/pelican-bootstrap3/static/css/custom.css': {'path': CUSTOM_CSS}
}

# Open Graph
OPEN_GRAPH_IMAGE = 'images/extra/site_open_graph.png'
TWITTER_USERNAME = "StevenMaude"
TWITTER_CARDS = True

FOOTER_SOCIAL = (('Twitter', 'https://twitter.com/StevenMaude'),
                 ('GitHub', 'https://github.com/StevenMaude'),
                 ('LinkedIn', 'https://linkedin.com/in/StevenMaude'),)
