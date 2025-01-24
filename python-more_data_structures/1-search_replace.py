#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for element in my_list:
        if element == search:
            # Ajoute élément de remplacement à new liste
            new_list.append(replace)
        else:
            # Sinon ajout élément d'origine à new liste
            new_list.append(element)
    return new_list
