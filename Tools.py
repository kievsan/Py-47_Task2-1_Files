import os

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
