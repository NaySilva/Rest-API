
# coding: utf-8

# In[1]:

import requests, json


# In[2]:

key = 'CHAVE API'
q = 'Bom dia, boa tarde e boa noite.'
target = 'en'


# In[3]:

url = 'https://translation.googleapis.com/language/translate/v2'
params = {'key':key, 'q':q, 'target':target}


# In[4]:

r = requests.get(url, params=params)


# In[5]:

r.status_code

# Out[5]:
'''
200
'''

# In[6]:

json.loads(r.text)

# Out[6]:

'''
{'data': {'translations': [{'detectedSourceLanguage': 'pt',
    'translatedText': 'Good morning, good afternoon and good evening.'}]}}
'''

# In[7]:

json.loads(r.text)['data']['translations'][0]['translatedText']


# Out[7]:

'''
'Good morning, good afternoon and good evening.'
'''



