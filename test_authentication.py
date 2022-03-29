import os
import requests



#################################
''' Function fct_test_authentication
to verify authentication
Parameters in string type : username, password
Results : output from command request on API http://172.17.0.2:8000/permissions
Write to file when environmental variable LOG==1
'''

def get_authentication(username: str, password: str):
  print("username : ", username)
    # requête
  r = requests.get(
      url = url_permissions,
      params= {'username': username,
               'password': password}
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

  # impression dans un fichier

  if os.environ.get('LOG') == '1':
    with open('log.txt', 'a') as file:
      file.write("\n" + "Test authentication :" + url_permissions + "\n")
      file.write(username + "\n")
      file.write(str(output))
      file.write("\n" + str(status_code) + " : " + test_status + "\n")


##########################################
'''
verification des permissions
'''

url_permissions = 'http://172.28.1.1:8000/permissions'
get_authentication("alice", "wonderland")
get_authentication("bob", "builder")
get_authentication("clementine", "mandarine")
