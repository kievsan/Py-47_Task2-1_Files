# PD-47
# PY-47
# Task211
# 2.1 Files - oткрытие и чтение файла, запись в файл
# https://github.com/netology-code/py-homeworks-basic/blob/new_oop/7.files/README.md

from pprint import pprint
import Tools


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

    print(f'\nЗадание: список блюд dishes_list: {dishes_list}')
    print(f'         кол-во блюд person_count: {person_count}\n')

    cookbook_dict = Tools.get_cookbook()

    ingredients_result_dict = {}
    for one_dish in dishes_list:
        if one_dish in cookbook_dict:
            one_dish_ingredients_dict = get_one_dish_ingredients_dict(cookbook_dict[one_dish])
            print(f'{one_dish} на {person_count} персон:')  #####
            for ingredient in one_dish_ingredients_dict:
                one_ingredient_measures_dict = one_dish_ingredients_dict[ingredient]
                new_quantity = get_multi_quantity(one_ingredient_measures_dict['quantity'], person_count)
                if ingredient in ingredients_result_dict:
                    general_quantity = ingredients_result_dict[ingredient]['quantity']
                    new_quantity = get_addition_quantity(new_quantity, general_quantity)
                one_ingredient_measures_dict['quantity'] = new_quantity
                ingredients_result_dict[ingredient] = one_ingredient_measures_dict
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
        try:
            new_key = ingredients_dict['ingredient_name']
            temp_dict = dict(ingredients_dict)
            del temp_dict['ingredient_name']
            result_dict[new_key] = temp_dict
        except KeyError as ex:
            print(f"Нет записи с ключём 'ingredient_name',  new_key: '{new_key}'")
            print(f'{ex}\n')
            exit(1)
        except Exception as other:
            print(f"Something else broke: {other}")
            exit(1)
    return result_dict


if __name__ == '__main__':
    print(f'\nЗАДАНИЕ 1:\tCook_book = ')
    pprint(Tools.get_cookbook())

    print(f'\n\nЗАДАНИЕ 2: Блюда')
    pprint(get_shop_dict_by_dishes(['Фахитос', 'Омлет'], 2))
    pprint(get_shop_dict_by_dishes(['Омлет'], 2))
    pprint(get_shop_dict_by_dishes(['Омлет', 'Омлет'], 1))
    pprint(get_shop_dict_by_dishes(['Утка по-пекински', 'Запеченный картофель'], 100))

    print(f'\n\nЗАДАНИЕ 3: Файлы')
    filenames_list = Tools.get_list_of_directory_files_by_template('[0-9]*.txt')
    print(f'\nСписок файлов для конкатенации: {filenames_list}')
    for filename in filenames_list:
        print(f'\n\t{filename}')
        Tools.print_txt_file(filename)

    sorted_fileheads_list = Tools.get_sorted_list_of_files_by_rule_1(filenames_list)
    print(f'\nСписок файлов в необходимом порядке для конкатенации: {sorted_fileheads_list}')

    cat_file_name = 'general.cat'
    Tools.cat(sorted_fileheads_list, cat_file_name)
    print(f'\n\t{cat_file_name}')
    Tools.print_txt_file(cat_file_name)

