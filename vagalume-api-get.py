
# coding: utf-8

# In[1]:

import requests, json


# In[2]:

url = 'https://api.vagalume.com.br/rank.php'
params = {'type':'mus','period':'month',
          'periodVal':'201707', 'limit':'3'}


# In[3]:

r = requests.get(url, params=params)


# In[4]:

json.loads(r.text)['mus']['month']['all']

# Out[4]:
''' 
[{'art': {'id': '3ade68b6g571beda3',
   'name': 'Luis Fonsi',
   'pic_medium': 'https://s2.vagalume.com/luis-fonsi/images/luis-fonsi.jpg',
   'pic_small': 'https://s2.vagalume.com/luis-fonsi/images/profile.jpg',
   'url': 'https://www.vagalume.com.br/luis-fonsi/'},
  'id': '3ade68b8g0317b0b3',
  'name': 'Despacito (Feat. Daddy Yankee)',
  'rank': '108.3',
  'uniques': '270324',
  'url': 'https://www.vagalume.com.br/luis-fonsi/despacito-feat-daddy-yankee.html',
  'views': '313384'},
 {'art': {'id': '3ade68b6g571beda3',
   'name': 'Luis Fonsi',
   'pic_medium': 'https://s2.vagalume.com/luis-fonsi/images/luis-fonsi.jpg',
   'pic_small': 'https://s2.vagalume.com/luis-fonsi/images/profile.jpg',
   'url': 'https://www.vagalume.com.br/luis-fonsi/'},
  'id': '3ade68b8g0317b0b3',
  'name': 'Despacito (Feat. Daddy Yankee) (tradução)',
  'rank': '79.0',
  'uniques': '197186',
  'url': 'https://www.vagalume.com.br/luis-fonsi/despacito-feat-daddy-yankee-traducao.html',
  'views': '217742'},
 {'albd': 'Teto Baixo',
  'alburl': 'teto-baixo',
  'alby': '2017',
  'art': {'id': '3ade68b7g9b450ea3',
   'name': 'Haikaiss',
   'pic_medium': 'https://s2.vagalume.com/haikaiss/images/haikaiss.jpg',
   'pic_small': 'https://s2.vagalume.com/haikaiss/images/profile.jpg',
   'url': 'https://www.vagalume.com.br/haikaiss/'},
  'id': '3ade68b8gcfbab0b3',
  'name': 'Rap Lord',
  'rank': '42.2',
  'uniques': '105269',
  'url': 'https://www.vagalume.com.br/haikaiss/rap-lord.html',
  'views': '121230'}]
'''


# In[5]:

for mus in json.loads(r.text)['mus']['month']['all']:
    print('%s - %s' % (mus['name'], mus['art']['name']))


# On[5]:
'''
Despacito (Feat. Daddy Yankee) - Luis Fonsi
Despacito (Feat. Daddy Yankee) (tradução) - Luis Fonsi
Rap Lord - Haikaiss
'''



