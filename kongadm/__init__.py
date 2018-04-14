# -*- coding:utf-8 -*-
# !/usr/bin/env python
#
# Author: daisheng
# Email: shawntai.ds@gmail.com

"""Top-level package for Python Kong Management."""


try:
    import imp
except ImportError:
    import importlib as imp

__version__ = '0.1'
__kong_version__ = '0.12.1'
__author__ = 'daisheng'

_KONGADM_URL = None
_KONGADM_APIKEY = None
_KONGADM_BASICAUTH = None
_USE_SESSION = True
_LOGLEVEL = 'ERROR'

import utils
import baseinf
import kongadm
from kongadm import Consumer, Group, JwtCred, node


def set_conf(kongadm_url=None, apikey=None, basicauth=None, use_session=None, loglevel=None):
    global _KONGADM_URL
    global _KONGADM_APIKEY
    global _KONGADM_BASICAUTH
    global _USE_SESSION
    global _LOGLEVEL
    global Consumer
    global Group
    global JwtCred
    global node
    if kongadm_url is not None:
        _KONGADM_URL = kongadm_url
    if apikey is not None:
        _KONGADM_APIKEY = apikey
    if basicauth is not None:
        _KONGADM_BASICAUTH = basicauth
    if use_session is not None:
        _USE_SESSION = use_session
    if loglevel is not None:
        _LOGLEVEL = loglevel
    imp.reload(utils)
    imp.reload(baseinf)
    imp.reload(kongadm)
    from kongadm import Consumer, Group, JwtCred, node
