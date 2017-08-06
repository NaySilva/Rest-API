# Web-APIs
## Google Translation API
Com Google Translate API é possível detectar idiomas e traduzir dinamicamente texto entre milhares de pares de idiomas. Ela não
é gratuita, e sua cobrança é baseado no uso de caracteres.

Para a demonstração foi utilizado o pacote googleapiclient. Neste pacote poderá utilizar o serviço da API. São necessários 
dois parâmetros de consulta com cada pedido de tradução:
* Idioma de destino: use o parâmetro “target” para especificar o idioma em que deseja traduzir.
* Cadeia de texto de origem: use o parâmetro “q” para especificar cada seqüência de texto para traduzir.

Além desses parâmetros tem diversos outros que são opcionais, como o “source”. No parâmetro “source” deve ser especificado o 
idioma do texto em “q”. Se o parâmetro não for definido, a API faz a detecção.
### Demonstração
```python

# coding: utf-8

# In[1]:

from googleapiclient.discovery import build
cliente = 'CHAVE DA API'
service = build('translate', 'v2', developerKey=cliente)
mensagem = 'Bom dia, boa tarde e boa noite.'


# In[2]:

lista = service.translations().list(target='en',q=mensagem).execute()


# In[3]:

lista

# Out[3]:

'''
{'translations': [{'detectedSourceLanguage': 'pt', 
'translatedText': 'Good morning, good afternoon and good evening.'}]}
'''

# In[4]:

idioma = lista['translations'][0]['detectedSourceLanguage']


# In[5]:

idioma

# Out[5]:

'''
'pt'
'''

# In[6]:

traducao = lista['translations'][0]['translatedText']


# In[7]:

traducao


# Out[7]:

'''
'Good morning, good afternoon and good evening.'
'''
```

## Twitter API
Com essa API é possível manipular quatro objetos do Twitter: tweets, usuários, entidades e os lugares. Na pesquisa de tweet 
pode ser encontrado as informações do usuário criador, as coordenadas da localização registrada no tweet, a data de criação,
a quantidade de retweets, as entidades (Hashtags, URLs, Usuários Mencionados, etc), o texto, etc.

Para utilizar a API tem que obter as chaves por meio de uma aplicação do usuário em https://apps.twitter.com/ ou por 
identificação do usuário.

### Demonstração

A demonstração foi feita através do pacote twitter. A figura abaixo demonstrar textos de três tweets que tenha a palavra
“Brasil”.

```python

# coding: utf-8

# In[1]:

import twitter


# In[2]:

CONSUMER_KEY = 'CONSUMER KEY'
CONSUMER_SECRET = 'CONSUMMER SECRET'
OAUTH_TOKEN = 'OAUTH TOKEN'
OAUTH_TOKEN_SECRET = 'OAUTH TOKEN SECRET'


# In[3]:

auth = twitter.oauth.OAuth(OAUTH_TOKEN, 
                           OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, 
                           CONSUMER_SECRET)


# In[4]:

t = twitter.Twitter(auth=auth)
search_results = t.search.tweets(q='Brasil', count=3, lang='pt')


# In[5]:

i = 0
for s in search_results['statuses']:
    i+=1
    print('%d - %s' % (i, s['text']))


# Out[5]:

'''
1 - Gol do melhor lateral do Brasil
2 - ARANA E FAGNER MELHORES LATERAIS DO BRASIL SIM TAO VOANDO
3 - RT @_Twittei_: "No Brasil não tem mulher bonita"
ATA https://t.co/YrhEMTNbyj
'''

```
## Vagalume API
Essa API possibilita a visualização das informações sobre artistas, letras de músicas, rankings e diversas outras coisas. 
Além disso é possível realizar buscar desses objetos. O uso da API é totalmente gratuito.
### Demonstração
Para uma demonstração rápida foi utilizado o pacote vagalume na busca de uma letra de música. Os campos “artist_name” e
“song_name” se trata respectivamente do nome do cantor ou banda e o nome da música.

```python

# coding: utf-8

# In[1]:

from vagalume import lyrics


# In[2]:

artist_name = 'coldplay'
song_name = 'viva la vida'


# In[3]:

result = lyrics.find(artist_name, song_name)


# In[4]:

if result.is_not_found():
    print('Song not sound')
else:
    print('%s - %s\n' % (result.song.name, result.artist.name))
    print(result.song.lyric)


# Out[4]:
'''
Viva La Vida - Coldplay

I used to rule the world
Seas would rise when I gave the word
Now in the morning I sleep alone
Sweep the streets I used to own

I used to roll the dice
Feel the fear in my enemy's eyes
Listen as the crowd would sing:
"Now the old king is dead!
Long live the king!"...
'''
```
