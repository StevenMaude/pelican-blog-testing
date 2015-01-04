#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Steven Maude'
SITENAME = u'stevenmaude.co.uk'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

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
SOCIAL = (('Twitter', 'https://twitter.com/StevenMaude'),
          ('LinkedIn', 'https://linkedin.com/in/StevenMaude'),
          ('GitHub', 'https://github.com/StevenMaude'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '/home/sm/Dev/pelican_blog/theme/pelican-bootstrap3'

# pelican-bootstrap3 specific configuration below here
BOOTSTRAP_THEME = 'flatly'
#BOOTSTRAP_NAVBAR_INVERSE = True

# Pygments
PYGMENTS_STYLE = 'monokai'

# Article info
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True

# Index page
DISPLAY_ARTICLE_INFO_ON_INDEX = True

# Sidebar
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_MAX_ITEMS = 10
#HIDE_SIDEBAR = True

# TODO: add favicon
#FAVICON = ''

# Content license
CC_LICENSE = "CC-BY-NC-SA"

# Open Graph
# TODO: add image
# OPEN_GRAPH_IMAGE = ''
TWITTER_USERNAME = "StevenMaude"
TWITTER_CARDS = True

# GitHub
#GITHUB_USER = 'StevenMaude'
#GITHUB_SKIP_FORK = True
#GITHUB_REPO_COUNT = 3
#GITHUB_SHOW_USER_LINK = False

# TODO: Related posts plugin
# TODO: Liquid tags plugin
#PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
#           'liquid_tags.youtube', 'liquid_tags.vimeo',
#           'liquid_tags.include_code', 'liquid_tags.notebook', ]

# TODO: Google Analytics
# GOOGLE_ANALYTICS_UNIVERSAL = ''
# GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = ''

# TODO: Addthis
# ADDTHIS_PROFILE = ''
