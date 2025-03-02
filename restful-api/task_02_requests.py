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
        posts = Response.json()
        print(posts)


def fetch_and_save_posts():
    """
    Cette fonction envoie une requête GET à l'API
    JSONPlaceholder pour récupérer
    une liste de posts.
    """

    url = 'https://jsonplaceholder.typicode.com/posts'
    Response = requests.get(url)
    if Response.status_code == 200:
        posts = Response.json()
        posts_list = [{'id': post['id'], 'title': post['title'],
                       'body': post['body']} for post in posts]
        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(posts_list)

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
