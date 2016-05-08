#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'KaiWang'
SITENAME = u"KaiWang's Page"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# THEME
THEME = u"alchemy"

# static
STATIC_PATHS = ['images']

# alchemy setting
#SITE_SUBTEXT = "Blabla"
PROFILE_IMAGE = "/images/peney_150x150.jpg"
GITHUB_ADDRESS = "https://github.com/kaiwang0112006"
LICENSE_NAME = "MIT"
LICENSE_URL = "https://opensource.org/licenses/MIT"
MENU_ITEMS = {}
#META_DESCRIPTION = "aph"
PAGES_ON_MENU = True
CATEGORIES_ON_MENU = True
TAGS_ON_MENU = True
ARCHIVES_ON_MENU = True
SHOW_ARTICLE_AUTHOR = False
