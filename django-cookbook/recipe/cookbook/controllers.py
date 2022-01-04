from .models import *


# MeasurmentUnit
def getallunits():
    units = MeasurmentUnit.objects.using('default')
    return units


def getunitbyid(pk):
    unit = MeasurmentUnit.objects.using('default').filter(id=pk)
    return unit


# Category
def getallcategories():
    categories = Category.objects.using('default')
    return categories


def getcategorybyid(pk):
    category = Category.objects.using('default').filter(id=pk)
    return category


# Course
def getallcourses():
    courses = Course.objects.using('default')
    return courses


def getcoursebyid(pk):
    course = Course.objects.using('default').filter(id=pk)
    return course


# Ingredient
def getallingredients():
    ingredients = Ingredient.objects.using('default')
    return ingredients


def getingredientbyid(pk):
    ingredient = Ingredient.objects.using('default').filter(id=pk)
    return ingredient


# Recipe
def getallrecipes():
    recipes = Recipe.objects.using('default')
    return recipes


def getrecipebyid(pk):
    recipe = Recipe.objects.using('default').filter(id=pk)
    return recipe


def getrecipe(pk):
    recipe = IngredientRecipe.objects.select_related('ingredient_id').select_related(
        'measurment_unit_id').select_related('recipe_id').filter(recipe_id=pk)
    return recipe


# IngredientRecipe
def getallingredientsrecipes():
    ingredients_recipes = IngredientRecipe.objects.using('default')
    return ingredients_recipes


def getingredientrecipebyid(pk):
    ingredient_recipe = IngredientRecipe.objects.using('default').filter(id=pk)
    return ingredient_recipe
