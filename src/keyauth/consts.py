#!/usr/bin/env python
# encoding: utf-8
from django.conf import settings

'''
DEFAULT VALUES
'''
DEFAULT_KEY_LAST_USED_UPDATE  = True
DEFAULT_KEY_EXPIRATION_DELTA  = 1
DEFAULT_KEY_PATTERN           = r"[a-z0-9A-Z]{30,40}"
DEFAULT_KEY_PARAMATER_NAME    = 'key'
DEFAULT_KEY_AUTH_401_TEMPLATE = None
DEFAULT_KEY_AUTH_401_CONTENT  = ""
DEFAULT_CONTENT_TYPE          = 'text/html; charset=utf-8'

'''
SETTINGS
'''
KEY_LAST_USED_UPDATE      = getattr(settings, 'KEY_LAST_USED_UPDATE', DEFAULT_KEY_LAST_USED_UPDATE)
KEY_EXPIRATION_DELTA      = getattr(settings, "KEY_EXPIRATION_DELTA", DEFAULT_KEY_EXPIRATION_DELTA)
KEY_PATTERN               = getattr(settings, "KEY_PATTERN", DEFAULT_KEY_PATTERN)
KEY_PARAMETER_NAME        = getattr(settings, 'KEY_PARAMETER_NAME', DEFAULT_KEY_PARAMATER_NAME)
KEY_AUTH_401_TEMPLATE     = getattr(settings, 'KEY_AUTH_401_TEMPLATE', DEFAULT_KEY_AUTH_401_TEMPLATE)
KEY_AUTH_401_CONTENT      = getattr(settings, 'KEY_AUTH_401_CONTENT', DEFAULT_KEY_AUTH_401_CONTENT)
KEY_AUTH_401_CONTENT_TYPE = getattr(settings, 'KEY_AUTH_401_CONTENT_TYPE', DEFAULT_CONTENT_TYPE)
