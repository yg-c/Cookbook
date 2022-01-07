from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *


def index(request):
    return render(request, 'index.html')


# Units
def measurementunits(request):
    units = MeasurementUnit.objects.using('default')
    return render(request, 'units.html', {'units': units})


def measurementunit(request, pk):
    unit = MeasurementUnit.objects.using('default').filter(id=pk)
    return render(request, 'unit.html', {'unit': unit})


def updateunit(request, pk):
    unit = MeasurementUnit.objects.using('default').filter(id=pk)

    # pré-remplissage du formulaire avec les données de l'object
    datas = {'id': unit[0].id, 'name': unit[0].name}
    form = UpdateUnitForm(datas)

    if request.method == 'POST':
        form = UpdateUnitForm(request.POST)
        if form.is_valid():
            unit_id = form.cleaned_data['id']
            name = form.cleaned_data['name']

            # écriture dans la base de donnée
            unit = MeasurementUnit(id=unit_id, name=name)
            unit.save(using='default')

            # renvoie de la liste
        return HttpResponseRedirect('/cookbook/units')

    return render(request, 'updateunit.html', {'form': form})


def addunit(request):
    form = AddUnitForm()
    if request.method == 'POST':
        form = AddUnitForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']

            # écriture dans la base de donnée
            unit = MeasurementUnit(name=name)
            unit.save(using='default')

            # renvoie de la liste
        return HttpResponseRedirect('/cookbook/units')

    return render(request, 'addunit.html', {'form': form})


def deleteunit(request, pk):
    MeasurementUnit.objects.using('default').filter(id=pk).delete()
    return HttpResponseRedirect('/cookbook/units')


# Recipes
def getallrecipes(request):
    recipes = Recipe.objects.using('default')
    return render(request, 'recipes.html', {'recipes': recipes})


def detailselectedrecipe(request, pk):
    recipe = IngredientRecipe.objects.select_related('ingredient_id').select_related(
        'measurement_unit_id').select_related('recipe_id').filter(recipe_id=pk)
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


# Ingredients
def getallingredients(request):
    ingredients = Ingredient.objects.using('default')
    return render(request, 'units.html', {'units': ingredients})
