import os
import requests

def get_content(url_sentiment : str, username: str, password: str, sentence: str):
  print("username : ", username)
    # requête
  r = requests.get(
      url = url_sentiment,
      params= {'username': username,
               'password': password,
               'sentence': sentence}
               )
  output = r.json()
  print(output) 

  if os.environ.get('LOG') == '1':
    with open('log.txt', 'a') as file:
        file.write("\n" + "Test de l'analyse du contenu : " + url_sentiment + "\n")
        file.write(username + "\n")
        file.write(sentence + "\n")
        file.write(str(output['score']) + "\n")

##############################
''' Verifier le score de chaque version
'''
#les 2 points d'entree de l'API
url_v1 = 'http://172.28.1.1:8000/v1/sentiment'
url_v2 = 'http://172.28.1.1:8000/v2/sentiment'
sentence_1 = 'life is beautiful'
sentence_2 = 'that sucks'

get_content(url_v1, 'alice', 'wonderland', sentence_1)
get_content(url_v2, 'alice', 'wonderland', sentence_1)

get_content(url_v1, 'alice', 'wonderland', sentence_2)
get_content(url_v2, 'alice', 'wonderland', sentence_2)
