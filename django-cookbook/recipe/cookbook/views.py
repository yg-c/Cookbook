from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from django.db.models import ProtectedError


# region index
def index(request):
    recipes = Recipe.objects.using('default')
    return render(request, 'index.html', {'recipes': recipes})
# endregion index


# region units
def measurementunits(request):
    units = MeasurementUnit.objects.using('default')

    # unités utilisées dans une recette
    units_ids = list(units.values_list('id', flat=True))
    ingredient_recipe_units = IngredientRecipe.objects.filter(measurement_unit_id__in=units_ids)
    unit_used = list(ingredient_recipe_units.values_list('measurement_unit_id', flat=True))
    # remove duplicates
    unit_used = dict.fromkeys(unit_used)
    unit_used = list(unit_used)

    for unit in units:
        if unit.id in unit_used:
            unit.used = 1
        else:
            unit.used = 0

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
    try:
        MeasurementUnit.objects.using('default').filter(id=pk).delete()
        return HttpResponseRedirect('/cookbook/units')
    except ProtectedError:
        return HttpResponseRedirect('/cookbook/units')
# endregion Units


# region recipes
def getallrecipes(request):
    recipes = Recipe.objects.using('default')
    return render(request, 'recipes.html', {'recipes': recipes})


def detailselectedrecipe(request, pk, nbr_people):
    recipe = IngredientRecipe.objects.select_related('ingredient_id').select_related(
        'measurement_unit_id').select_related('recipe_id').filter(recipe_id=pk)
    name = recipe[0].recipe_id.name
    pax = recipe[0].recipe_id.pax
    category = recipe[0].recipe_id.category_id.name
    course = recipe[0].recipe_id.course_id.name
    preparation_time = recipe[0].recipe_id.preparation_time
    instructions = recipe[0].recipe_id.instructions
    ingredients = recipe

    # ajuster les mesures par rapport au pax
    for ingredient in ingredients:
        ingredient.quantity = ingredient.quantity/pax*nbr_people

    return render(request, 'recipe.html',
                  {'recipe': recipe, 'name': name, 'pax': nbr_people, 'category': category, 'course': course,
                   'preparation_time': preparation_time, 'instructions': instructions, 'ingredients': ingredients})


def deleterecipe(request, pk):
    Recipe.objects.using('default').filter(id=pk).delete()
    return HttpResponseRedirect('/cookbook/recipes')

def addrecipe(request):
    form = AddRecipeForm()
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']

            # écriture dans la base de donnée
            recipe = Recipe(name=name)
            recipe.save(using='default')

            # renvoie de la liste
        return HttpResponseRedirect('/cookbook/recipes')
    return render(request, 'addrecipe.html', {'form': form})    
# endregion recipes


# region ingredients
def getallingredients(request):
    ingredients = Ingredient.objects.using('default')

    # ingrédients utilisés dans une recette
    ingredients_ids = list(ingredients.values_list('id', flat=True))
    ingredient_recipe_units = IngredientRecipe.objects.filter(ingredient_id__in=ingredients_ids)
    ingredients_used = list(ingredient_recipe_units.values_list('ingredient_id', flat=True))
    # remove duplicates
    ingredients_used = dict.fromkeys(ingredients_used)
    ingredients_used = list(ingredients_used)

    for ingredient in ingredients:
        if ingredient.id in ingredients_used:
            ingredient.used = 1
        else:
            ingredient.used = 0

    return render(request, 'ingredients.html', {'ingredients': ingredients})


def addingredient(request):
    form = AddIngredientForm()
    if request.method == 'POST':
        form = AddIngredientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']

            # écriture dans la base de donnée
            ingredient = Ingredient(name=name)
            ingredient.save(using='default')

            # renvoie de la liste
        return HttpResponseRedirect('/cookbook/ingredients')
    return render(request, 'addingredient.html')


def deleteingredient(request, pk):
    try:
        Ingredient.objects.using('default').filter(id=pk).delete()
        return HttpResponseRedirect('/cookbook/ingredients')
    except ProtectedError:
        return HttpResponseRedirect('/cookbook/ingredients')


def updateingredient(request, pk):
    ingredient = Ingredient.objects.using('default').filter(id=pk)

    # pré-remplissage du formulaire avec les données de l'object
    datas = {'id': ingredient[0].id, 'name': ingredient[0].name}
    form = UpdateIngredientForm(datas)

    if request.method == 'POST':
        form = UpdateIngredientForm(request.POST)
        if form.is_valid():
            ingredient_id = form.cleaned_data['id']
            ingredient_name = form.cleaned_data['name']

            # écriture dans la base de donnée
            ingredient = Ingredient(id=ingredient_id, name=ingredient_name)
            ingredient.save(using='default')

            # renvoie de la liste
        return HttpResponseRedirect('/cookbook/ingredients')

    return render(request, 'updateingredient.html', {'form': form})
# endregion ingredients


# region courses
def getallcourses(request):
    courses = Course.objects.using('default')

    # courses utilisées dans une recette
    courses_ids = list(courses.values_list('id', flat=True))
    recipe_courses = Recipe.objects.filter(course_id__in=courses_ids)
    courses_used = list(recipe_courses.values_list('course_id', flat=True))
    # remove duplicates
    courses_used = dict.fromkeys(courses_used)
    courses_used = list(courses_used)

    for course in courses:
        if course.id in courses_used:
            course.used = 1
        else:
            course.used = 0

    return render(request, 'courses.html', {'courses': courses})


def addcourse(request):
    form = AddCourseForm()
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']

            # écriture dans la base de donnée
            course = Course(name=name)
            course.save(using='default')

            # renvoie de la liste
        return HttpResponseRedirect('/cookbook/courses')

    return render(request, 'addcourse.html', {'form': form})


def updatecourse(request, pk):
    unit = Course.objects.using('default').filter(id=pk)

    # pré-remplissage du formulaire avec les données de l'object
    datas = {'id': unit[0].id, 'name': unit[0].name}
    form = UpdateCourseForm(datas)

    if request.method == 'POST':
        form = UpdateCourseForm(request.POST)
        if form.is_valid():
            unit_id = form.cleaned_data['id']
            name = form.cleaned_data['name']

            # écriture dans la base de donnée
            unit = Course(id=unit_id, name=name)
            unit.save(using='default')

            # renvoie de la liste
        return HttpResponseRedirect('/cookbook/courses')

    return render(request, 'updatecourse.html', {'form': form})


def deletecourse(request, pk):
    Course.objects.using('default').filter(id=pk).delete()
    return HttpResponseRedirect('/cookbook/courses')
# endregion courses


# region categories
def getallcategories(request):
    categories = Category.objects.using('default')

    # courses utilisées dans une recette
    categories_ids = list(categories.values_list('id', flat=True))
    recipe_categories = Recipe.objects.filter(category_id__in=categories_ids)
    categories_used = list(recipe_categories.values_list('category_id', flat=True))
    # remove duplicates
    categories_used = dict.fromkeys(categories_used)
    categories_used = list(categories_used)

    for category in categories:
        if category.id in categories_used:
            category.used = 1
        else:
            category.used = 0

    return render(request, 'categories.html', {'categories': categories})


def addcategory(request):
    form = AddCategoryForm()
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']

            # écriture dans la base de donnée
            category = Category(name=name)
            category.save(using='default')

            # renvoie de la liste
        return HttpResponseRedirect('/cookbook/categories')

    return render(request, 'addcategory.html', {'form': form})


def updatecategory(request, pk):
    unit = Category.objects.using('default').filter(id=pk)

    # pré-remplissage du formulaire avec les données de l'object
    datas = {'id': unit[0].id, 'name': unit[0].name}
    form = UpdateCategoryForm(datas)

    if request.method == 'POST':
        form = UpdateCategoryForm(request.POST)
        if form.is_valid():
            unit_id = form.cleaned_data['id']
            name = form.cleaned_data['name']

            # écriture dans la base de donnée
            unit = Category(id=unit_id, name=name)
            unit.save(using='default')

            # renvoie de la liste
        return HttpResponseRedirect('/cookbook/categories')

    return render(request, 'updatecategory.html', {'form': form})


def deletecategory(request, pk):
    Category.objects.using('default').filter(id=pk).delete()
    return HttpResponseRedirect('/cookbook/categories')
# endregion categories
