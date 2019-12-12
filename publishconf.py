#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://www.stevenmaude.co.uk'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_MAX_ITEMS = 10
FEED_DOMAIN = SITEURL

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
