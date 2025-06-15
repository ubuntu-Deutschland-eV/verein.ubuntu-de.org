#!/usr/bin/env python

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://verein.ubuntu-de.org'
RELATIVE_URLS = False

PLUGINS += [ #'minify', # disable due to https://github.com/pelican-plugins/minify/issues/6
             'gzip_cache',
             ]

DELETE_OUTPUT_DIRECTORY = True
