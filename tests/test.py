# -*- coding:utf-8 -*-
# !/usr/bin/env python
#
# Author: Shawn.T
# Email: shawntai.ds@gmail.com
#

import sys, json
sys.path.append('..')

from utils import *
import json
import os
import kongadm
from kongadm.client import Client, Session
from mock import Mock, patch


class TestClient():
    def setUp(self):
        kongadm.set_conf('http://testkongadm_url')

    def tearDown(self):
        pass

    @staticmethod
    def mock_resp(status_code=200, encoding='utf-8', content=dict(message='test results')):
        resp_dict = dict(
            status_code=status_code,
            encoding=encoding,
            content=json.dumps(content)
            )
        return Mock(return_value=Options(**resp_dict))

    @with_setup(setUp, tearDown)
    def test_client(self):
        """
        [client    ]kongadm.client
        """
        with patch.object(Session, 'request', self.mock_resp()):
            basic_auth = dict(username='username', password='password')
            kong_client = Client('http://testip.com', basic_auth=basic_auth, use_session=True)
            data = kong_client._execute('GET', 'testpath/', None)
            kong_client.destroy()
            assert 'message' in data

    @with_setup(setUp, tearDown)
    def test_baseinf_nodeinf(self):
        """
        [baseinf    ]kongadm.baseinf.nodeinf
        """
        content = dict(version='123')
        with patch.object(Session, 'request', self.mock_resp(content=content)):
            with patch.object(Client, 'chk_conn', Mock(return_value=True)):
                kongadm.set_conf('http://testkongadm_url')
                data = kongadm.node.info
                assert 'version' in data
                data = kongadm.node.status
                assert 'version' in data

    @with_setup(setUp, tearDown)
    def test_baseinf_consumerinf(self):
        """
        [baseinf    ]kongadm.baseinf.consumerinf
        """
        content = dict(id='123')
        with patch.object(Session, 'request', self.mock_resp(content=content)):
            with patch.object(Client, 'chk_conn', Mock(return_value=True)):
                cinf = kongadm.baseinf.ConsumerInf()
                data = cinf.retrieve('123')
                assert '123' in data['id']
