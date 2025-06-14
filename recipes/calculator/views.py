from django.shortcuts import render
from typing import Dict

class RecipesData:
    data: Dict = {
            'omlet': {
                'яйца, шт': 2,
                'молоко, л': 0.1,
                'соль, ч.л.': 0.5,
            },
            'pasta': {
                'макароны, г': 0.3,
                'сыр, г': 0.05,
            },
            'buter': {
                'хлеб, ломтик': 1,
                'колбаса, ломтик': 1,
                'сыр, ломтик': 1,
                'помидор, ломтик': 1,
            },
            # можете добавить свои рецепты;)
            'salat': {
                'капуста, г': 150,
                'растительное масло, ст. ложка': 2,
                'соль, г': 2,
                'уксус 9%, ст. ложка': 2,
            }}

def recipes (request, recipe: str):
    template_name: str = 'calculator/index.html'
    num: int = int(request.GET.get("servings", 1))
    temp_data: Dict = {name:val*num for name, val in RecipesData.data.get(str(recipe)).items()}
    context: Dict = {'recipe':temp_data}
    return render(request, template_name, context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }