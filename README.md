# kongadm [![GitHub license](https://img.shields.io/github/license/seethedoor/kongadm.svg)](https://github.com/seethedoor/kongadm/blob/master/LICENSE) [![Version](https://img.shields.io/badge/version-0.1-green.svg)](https://img.shields.io/badge/version-0.1-green.svg)


a kong management python client

# USEAGE

## install kongadm package
* environment: python 2.7
* install:
```bash
$ pip install git+https://github.com/seethedoor/kongadm.git
```

## configurations
* use kongadm.set_conf() to do this
* `kongadm_url`(required) could be a string of your kongadmin API URL
* `apikey`(optional) your api key to access kongadm
* `basicauth`(optional) your basicauth infomation as a dict with 'username' and 'password'
* `use_session`(optional) Bollean type value, default as 'True'
* `loglevel`(optional) devfault as 'ERROR'
```bash
>>> import kongadm
>>> kongadm.set_conf(kongadm_url='your kongadmin API url')
```

## kong node status
```bash
>>> kongadm.node.info
>>> kongadm.node.status
```

## consumer
* use `kongadm.Consumer('your-username')` to create a new consumer
* use `kongadm.Consumer.get('your-username')` to get a exist consumer
```bash
>>> kongadm.Consumer.list_usernames()
>>> consumer = kongadm.Consumer('your-username')
# set groups property, etc..
>>> consumer.groups = ['group1', 'group2']
```
## group
```bash
>>> 
```

## api

## Jwtcredential

## token auth methods

