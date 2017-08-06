
# coding: utf-8

# In[1]:

import requests, json


# In[2]:

from requests_oauthlib import OAuth1Session


# In[3]:

CONSUMER_KEY = 'CONSUMER KEY'
CONSUMER_SECRET = 'CONSUMMER SECRET'
OAUTH_TOKEN = 'OAUTH TOKEN'
OAUTH_TOKEN_SECRET = 'OAUTH TOKEN SECRET'


# In[4]:

session = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


# In[5]:

status = 'Teste de atualização de status pelo Twitter API.'


# In[6]:

url = 'https://api.twitter.com/1.1/statuses/update.json'
params = {'status':status}


# In[7]:

r = session.post(url, params=params)


# In[8]:

json.loads(r.text)


# Out[8]:
'''
{'contributors': None,
 'coordinates': None,
 'created_at': 'Sun Aug 06 02:54:28 +0000 2017',
 'entities': {'hashtags': [], 'symbols': [], 'urls': [], 'user_mentions': []},
 'favorite_count': 0,
 'favorited': False,
 'geo': None,
 'id': 894028873012269057,
 'id_str': '894028873012269057',
 'in_reply_to_screen_name': None,
 'in_reply_to_status_id': None,
 'in_reply_to_status_id_str': None,
 'in_reply_to_user_id': None,
 'in_reply_to_user_id_str': None,
 'is_quote_status': False,
 'lang': 'pt',
 'place': None,
 'retweet_count': 0,
 'retweeted': False,
 'source': '<a href="" rel="nofollow"></a>',
 'text': 'Teste de atualização de status pelo Twitter API.',
 'truncated': False,
 'user': {'contributors_enabled': False,
  'created_at': 'Wed May 24 14:30:04 +0000 2017',
  'default_profile': True,
  'default_profile_image': True,
  'description': '',
  'entities': {'description': {'urls': []}},
  'favourites_count': 0,
  'follow_request_sent': False,
  'followers_count': 315,
  'following': False,
  'friends_count': 763,
  'geo_enabled': False,
  'has_extended_profile': False,
  'id': ,
  'id_str': '',
  'is_translation_enabled': False,
  'is_translator': False,
  'lang': 'pt',
  'listed_count': 0,
  'location': '',
  'name': '',
  'notifications': False,
  'profile_background_color': 'F5F8FA',
  'profile_background_image_url': None,
  'profile_background_image_url_https': None,
  'profile_background_tile': False,
  'profile_image_url': 'http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png',
  'profile_image_url_https': 'https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png',
  'profile_link_color': '1DA1F2',
  'profile_sidebar_border_color': 'C0DEED',
  'profile_sidebar_fill_color': 'DDEEF6',
  'profile_text_color': '333333',
  'profile_use_background_image': True,
  'protected': False,
  'screen_name': '',
  'statuses_count': 110,
  'time_zone': None,
  'translator_type': 'none',
  'url': None,
  'utc_offset': None,
  'verified': False}}
'''




