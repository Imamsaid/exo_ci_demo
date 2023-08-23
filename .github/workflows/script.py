from main import *
import requests


def dowload_file(url,dataset= "data_set"):
    reponse =requests.get(url)
    with open(dataset, 'wb') as file:
        file.write(reponse.content)