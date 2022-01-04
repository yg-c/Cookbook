# from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'index.html')


def measurmentunits(request):
    units = MeasurementUnit.objects.using('default')
    return render(request, 'units.html', {'units': units})


def measurmentunit(request, pk):
    unit = MeasurementUnit.objects.using('default').filter(id=pk)
    return render(request, 'unit.html', {'unit': unit})


def getallrecipes(request):
    recipes = Recipe.objects.using('default')
    return render(request, 'recipes.html', {'recipes': recipes})


def detailselectedrecipe(request, pk):
    recipe = IngredientRecipe.objects.select_related('ingredient_id').select_related(
        'measurment_unit_id').select_related('recipe_id').filter(recipe_id=pk)
    name = recipe[0].recipe_id.name
    pax = recipe[0].recipe_id.pax
    category = recipe[0].recipe_id.category_id.name
    course = recipe[0].recipe_id.course_id.name
    preparation_time = recipe[0].recipe_id.preparation_time
    instructions = recipe[0].recipe_id.instructions
    ingredients = recipe
    return render(request, 'recipe.html',
                  {'recipe': recipe, 'name': name, 'pax': pax, 'category': category, 'course': course,
                   'preparation_time': preparation_time, 'instructions': instructions, 'ingredients': ingredients})
