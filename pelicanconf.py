#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ross Barnowski'
SITENAME = u'NE204-Spring2018'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['pages', 'downloads']

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# For site theme
# NOTE: Requires cloning of pelican-themes and pelican-plugins repos into
# /home/ross/repos
THEME = '/home/ross/repos/pelican-themes/pelican-bootstrap3'
PLUGIN_PATHS = ['/home/ross/repos/pelican-plugins',]
PLUGINS = ['i18n_subsites']
I18N_TEMPLATES_LANG = 'en'
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
