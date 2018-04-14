# -*- coding:utf-8 -*-
# !/usr/bin/env python
#
# Author: daisheng
# Email: shawntai.ds@gmail.com

import logging

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

from . import _LOGLEVEL
logger.setLevel(eval('logging.%s' % _LOGLEVEL))
