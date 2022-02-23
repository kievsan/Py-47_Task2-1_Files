# PD-47
# PY-47
# Task211
# 2.1 Files - oткрытие и чтение файла, запись в файл
# https://github.com/netology-code/py-homeworks-basic/blob/new_oop/7.files/README.md

import os
from pprint import pprint

_COOKBOOK = os.path.join(os.getcwd(), "recipes.data")


def get_cookbook(refresh=False):
    if refresh:
        get_cookbook.recipes_dict = {}
    if get_cookbook.recipes_dict:
        return get_cookbook.recipes_dict
    with open(_COOKBOOK, 'r', encoding='utf-8') as recipes_file:
        for recipe in recipes_file:
            recipe = recipe.strip()
            if not recipe:
                continue
            ingredients_number = int(recipes_file.readline().strip())
            one_dish_ingredients_list = []
            for ingredients in range(ingredients_number):
                ingredient_name, quantity, measure = recipes_file.readline().strip().split('|')
                one_dish_ingredients_list.append(
                    {'ingredient_name': ingredient_name,
                     'quantity': quantity,
                     'measure': measure})
            get_cookbook.recipes_dict[recipe] = one_dish_ingredients_list
            recipes_file.readline()
    return get_cookbook.recipes_dict


get_cookbook.recipes_dict = {}


def get_shop_dict_by_dishes(dishes_list, person_count):
    """
    :param dishes_list:
    :param dishes
     на вход принимает список блюд dishes из cook_book
    :param person_count
     и количество персон, для кого мы будем готовить

    На выходе мы должны получить словарь
    с названием ингредиентов и его количества для блюда.
    """
    try:
        cookbook_dict = get_cookbook()
    except Exception as ex:
        print(f'Ошибка! при повторном вызове "get_cookbook"')

    ingredients_result_dict = {}
    for one_dish in dishes_list:
        if one_dish in cookbook_dict:
            one_dish_ingredients_dict = get_one_dish_ingredients_dict(cookbook_dict[one_dish])
            print(f'\none_dish: {one_dish}')  #####
            pprint(one_dish_ingredients_dict)  #####

            print(f'\none_dish: {one_dish} на {person_count} персон:')  #####
            for ingredient in one_dish_ingredients_dict:
                one_ingredient_measures_dict = one_dish_ingredients_dict[ingredient]
                new_quantity = get_multi_quantity(one_ingredient_measures_dict['quantity'], person_count)
                one_ingredient_measures_dict['quantity'] = new_quantity  #####
                print(ingredient, one_ingredient_measures_dict)  #####
                if ingredient in ingredients_result_dict:
                    general_quantity = ingredients_result_dict[ingredient]['quantity']
                    new_quantity = get_addition_quantity(new_quantity, general_quantity)
                one_ingredient_measures_dict['quantity'] = new_quantity
                ingredients_result_dict[ingredient] = one_ingredient_measures_dict
            print()
    return ingredients_result_dict


def get_multi_quantity(quantity, multiplier):
    new_quantity = quantity
    try:
        int_quantity = int(quantity) * int(multiplier)
        new_quantity = ' ' + str(int_quantity) + ' '
    except ValueError as ex:
        print(f"Не кастятся к (int) строки quantity: '{quantity}' или multiplier: '{multiplier}'")
        print(f'{ex}\n')
    except Exception as other:
        print(f"Something else broke: {other}")
    return new_quantity


def get_addition_quantity(quantity, summand):
    new_quantity = quantity
    try:
        int_quantity = int(quantity) + int(summand)
        new_quantity = ' ' + str(int_quantity) + ' '
    except ValueError as ex:
        print(f"Не кастятся к (int) строки quantity:' {quantity}' или multiplier: {summand}")
        print(f'{ex}\n')
    except Exception as other:
        print(f"Something else broke: {other}")
    return new_quantity


def get_one_dish_ingredients_dict(ingredients_list):
    result_dict = {}
    for ingredients_dict in ingredients_list:
        new_key = ingredients_dict['ingredient_name']    ######   ошибка!
        # print(new_key, ingredients_dict)
        temp_dict = ingredients_dict
        del temp_dict['ingredient_name']
        result_dict[new_key] = temp_dict
    return result_dict


if __name__ == '__main__':
    print(f'\nCook_book = ')
    pprint(get_cookbook())

    # pprint(get_shop_dict_by_dishes(['Фахитос', 'Омлет'], 2))
    # pprint(get_shop_dict_by_dishes(['Фахитос', 'Омлет'], "Ого-го!"))

    pprint(get_shop_dict_by_dishes(['Омлет'], 2))
    # print(get_shop_dict_by_dishes(['Омлет', 'Омлет'], 1))

    # pprint(get_shop_dict_by_dishes(['Фахитос', 'Фахитос', 'Омлет', 'Омлет'], 1))
