import os
import requests

def get_authorization(url_sentiment : str, username: str, password: str, sentence: str):
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

  # statut de la requête
    status_code = r.status_code

  # affichage des résultats
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    print(str(status_code) + " : " + test_status)

    if os.environ.get('LOG') == '1':
      with open('log.txt', 'a') as file:
        file.write("\n" + "Test d'authorization " + url_sentiment + "\n")
        file.write(username + "\n")
        file.write(str(output))
        file.write("\n" + str(status_code) + " : " + test_status + "\n")

##############################
''' Verifier la logique de gestion des droits des utilisateurs 
'''
#les 2 points d'entree de l'API
url_v1 = 'http://172.28.1.1:8000/v1/sentiment'
url_v2 = 'http://172.28.1.1:8000/v2/sentiment'

get_authorization(url_v1,'alice', 'wonderland', 'life is beautiful')
get_authorization(url_v2,'alice', 'wonderland', 'life is beautiful')

get_authorization(url_v1,'bob', 'builder', 'life is beautiful')
get_authorization(url_v2,'bob', 'builder', 'life is beautiful')

get_authorization(url_v1,'clementine', 'mandarine', 'life is beautiful')
get_authorization(url_v2,'clementine', 'mandarine', 'life is beautiful')


