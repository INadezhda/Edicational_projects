import pprint


def cook_book_dict(file_name):
    with open(file_name, 'r', encoding='utf-8') as a:
        cook_book = {}
        for k in a:
            recept = k.strip()
            x = int(a.readline())
            cook = []
            for i in range(x):
                ingr = a.readline().split("|")
                ingredients = {'ingredient_name': ingr[0].strip(),
                               'quantity': int(ingr[1]),
                               'measure': ingr[2].strip()
                               }
                cook.append(ingredients)
            cook_book[recept] = cook
            a.readline()
        # print(cook_book)
    # for key,value in cook_book.items():
    #     print("{0}:\n {1}".format(key,value),'\n')
    pprint.pprint(cook_book, width=200)
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    x = {}
    for dish in dishes:
        for ingr in cook_book_dict(file_name).get(dish):
            a = ingr['ingredient_name']
            b = ingr.pop('ingredient_name', None)
            if a not in x.keys():
                ingr['quantity'] = ingr.get('quantity') * person_count
                x[a] = ingr
            else:
                ingr['quantity'] = x[a].get(
                    'quantity') + ((ingr['quantity']) * person_count)
                x[a] = ingr
    pprint.pprint(x, width=200)
    return x


file_name = 'cook_book.txt'
cook_book_dict(file_name)
dishes = ['Омлет', 'Фахитос']
person_count = int(5)
get_shop_list_by_dishes(dishes, person_count)
