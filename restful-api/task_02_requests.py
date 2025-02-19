import requests
import csv

def fetch_and_print_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    Response = requests.get(url)
    if Response.status_code == 200:
        todo = Response.json()
        print(todo)

def fetch_and_save_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    Response = requests.get(url)
    if Response.status_code == 200:
        todo = Response.json()
        print(todo)
