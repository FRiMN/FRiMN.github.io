#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Freezeman'
SITENAME = u'Магия на кончиках пальцев'
SITEURL = ''

PATH = '../'
# ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{slug}.html'
ARTICLE_URL = '{category}/{date:%Y}/{slug}.html'


# THEME = "/home/freezeman/pelican-themes/pelican-twitchy"
# THEME = "/home/freezeman/pelican-themes/monospace"
# THEME = "/home/freezeman/pelican-themes/bricks"
# THEME = "/home/freezeman/pelican-themes/chunk"
# THEME = "/home/freezeman/pelican-themes/clean-blog"
# THEME = "/home/freezeman/pelican-themes/Flex"
# THEME = "/home/freezeman/pelican-themes/medius"
# THEME = "/home/freezeman/pelican-themes/nest"   # backgroud-position: center 20%; background-size: cover;
# THEME = "/home/freezeman/pelican-themes/nmnlist"
# THEME = "/home/freezeman/pelican-themes/Nuja"
# THEME = "/home/freezeman/pelican-themes/pelican-cait"
# THEME = "/home/freezeman/pelican-themes/w3-personal-blog"
# THEME = "/home/freezeman/pelican-themes/Casper2Pelican"
# THEME = "/home/freezeman/pelican-themes/mediumfox"
# THEME = "/home/freezeman/pelican-themes/pelipress"
# THEME = "/home/freezeman/pelican-themes/pure"
# THEME = "/home/freezeman/pelican-themes/sundown"
# THEME = "/home/freezeman/pelican-themes/storm"
THEME = "/home/freezeman/projects/singularity"


# PLUGIN_PATHS = ['/home/freezeman/pelican-plugins']
# PLUGINS = ['extract_toc']


TIMEZONE = 'Asia/Krasnoyarsk'

DEFAULT_LANG = u'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    # ('Pelican', 'http://getpelican.com/'),
    # ('Python.org', 'http://python.org/'),
    # ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (
    ('Bitbucket', 'https://bitbucket.org/FRiMN/'),
    ('GitHub', 'https://github.com/FRiMN'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
