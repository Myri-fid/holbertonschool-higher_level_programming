import requests
import csv

"""
 Cette fonction envoie une requête GET à l'API JSONPlaceholder pour récupérer
une liste de posts.
"""


def fetch_and_print_posts():
    """
    Cette fonction envoie une requête GET à l'API
    JSONPlaceholder pour récupérer
    une liste de posts.
    """

    url = 'https://jsonplaceholder.typicode.com/posts'
    Response = requests.get(url)
    if Response.status_code == 200:
        todo = Response.json()
        print(todo)


def fetch_and_save_posts():
    """
    Cette fonction envoie une requête GET à l'API
    JSONPlaceholder pour récupérer
    une liste de posts.
    """

    url = 'https://jsonplaceholder.typicode.com/posts'
    Response = requests.get(url)
    if Response.status_code == 200:
        todo = Response.json()
        print(todo)
