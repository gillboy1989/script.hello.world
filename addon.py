import logging
import xbmcaddon
from . import kodilogging
from . import kodiutils
from . import settings

import sys

from urllib import urlencode
from urllib import quote
from urlparse import parse_qsl

from datetime import datetime

import xbmcgui
import xbmcplugin
import xbmc

import requests
import itertools
import operator

import time
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = "Alt Bala ji Addon!"
line2 = "We can write anything we want here"
line3 = "Using Python"
 
xbmcgui.Dialog().ok(addonname, line1, line2, line3)

logger = logging.getLogger(ADD_ON.getAddonInfo('id'))
kodilogging.config(logger)


