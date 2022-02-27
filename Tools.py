import os
import glob

_COOKBOOK = os.path.join(os.getcwd(), "recipes.data")


def get_cookbook(refresh=False):
    if refresh:
        get_cookbook.recipes_dict = {}
    if get_cookbook.recipes_dict:
        return get_cookbook.recipes_dict
    try:
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
    except FileNotFoundError as ex:
        print(f'File "{recipes_file}" not found...\n\t{ex}\n')
    except OSError as other:
        print(f'При открытии файла "{recipes_file}" возникли проблемы: \n\t{other}\n')
    return get_cookbook.recipes_dict


get_cookbook.recipes_dict = {}


def print_txt_file(file_name):
    # Печать файла 'как есть':
    print()
    try:
        with open(file_name, 'r', encoding='utf-8') as txt_file:
            for line in txt_file:
                l = line.strip()
                if not l:
                    continue
                print(l)
    except FileNotFoundError as ex:
        print(f'File "{file_name}" not found...\n\t{ex}\n')
    except OSError as other:
        print(f'При открытии файла "{file_name}" возникли проблемы: \n\t{other}\n')


def cat(head_list, cat_file_name):
    try:
        with open(cat_file_name, 'w', encoding='utf-8') as cat_file:
            # Файлы сцепляются в порядке следования элементов списка:
            for adding_file_head_tuple in head_list:
                filename, lines_count = adding_file_head_tuple
                try:
                    with open(filename, 'r', encoding='utf-8') as add_file:
                        cat_file.write(filename + '\n')
                        cat_file.write(str(lines_count) + '\n')
                        for line in add_file:
                            cat_file.write(line)
                except FileNotFoundError as ex:
                    print(f'File "{add_file}" not found...\n\t{ex}\n')
                except OSError as other:
                    print(f'При открытии файла "{add_file}" возникли проблемы: \n\t{other}\n')
    except FileNotFoundError as ex:
        print(f'File "{cat_file}" not found...\n  {ex}\n')
    except OSError as other:
        print(f'При открытии файла "{cat_file}" возникли проблемы: \n\t{other}\n')


def get_sorted_list_of_files_by_rule_1(files_list):
    head_dict = dict()
    for filename in files_list:
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                line_counter = 0
                for line in f:
                    line_counter += 1
        except FileNotFoundError as ex:
            print(f'File "{filename}" not found...\n\t{ex}\n')
            exit(1)
        except OSError as other:
            print(f'При открытии файла "{filename}" возникли проблемы: \n\t{other}\n')
            exit(1)
        else:
            head_dict[filename] = line_counter

    head_list = list(head_dict.items())
    head_list.sort(key=lambda i: i[1])
    return head_list


def get_list_of_directory_files_by_template(template):
    return sorted(glob.glob(template))
