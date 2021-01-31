#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Yuchi Yang'
SITENAME = "Yuchi's Blog"
SITEURL = ''
SITE_DESCRIPTION = '''This is my personal blog.'''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


# Pelican default theme for dev
THEME = "theme"
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'blog']