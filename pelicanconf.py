#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Steven Maude'
SITENAME = u'stevenmaude.co.uk'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
#SOCIAL = (('Twitter', 'https://twitter.com/StevenMaude'),
#          ('LinkedIn', 'https://linkedin.com/in/StevenMaude'),
#          ('GitHub', 'https://github.com/StevenMaude'),)
FOOTER_SOCIAL = (('Twitter', 'https://twitter.com/StevenMaude'),
                 ('GitHub', 'https://github.com/StevenMaude'),
                 ('LinkedIn', 'https://linkedin.com/in/StevenMaude'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# TODO: Liquid tags plugin or PyEmbed
PLUGINS = ['pelican_alias', ]

THEME = 'theme/pelican-bootstrap3'

# pelican-bootstrap3 specific configuration below here
BOOTSTRAP_THEME = 'flatly'
BOOTSTRAP_NAVBAR_INVERSE = True

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

# Sidebar
#DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_MAX_ITEMS = 10
#HIDE_SIDEBAR = True

STATIC_PATHS = ['images', 'extra/favicon.ico', 'extra/site_open_graph.png']

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# Content license
CC_LICENSE = "CC-BY-NC-SA"

# Open Graph
OPEN_GRAPH_IMAGE = 'extra/site_open_graph.png'
TWITTER_USERNAME = "StevenMaude"
TWITTER_CARDS = True

# GitHub
#GITHUB_USER = 'StevenMaude'
#GITHUB_SKIP_FORK = True
#GITHUB_REPO_COUNT = 3
#GITHUB_SHOW_USER_LINK = False

# TODO: Addthis
# ADDTHIS_PROFILE = ''
