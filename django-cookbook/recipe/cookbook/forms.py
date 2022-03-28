from django import forms
from django.forms import formset_factory

from .models import *


# region recipes

class AddRecipeForm(forms.Form):
    name = forms.CharField(label='Nom', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nom'
    })
                           )

    # Liste déroulante categories (liste ne peut-être que sous forme de tuples)
    categories = Category.objects.using('default')
    categories_name_list = []
    categories_id_list = []
    for categorie in categories:
        categories_id_list.append(categorie.id)
        categories_name_list.append(categorie.name)
    categories_tuples = list(zip(categories_id_list, categories_name_list))
    # Renvoi de l'id
    categories_choice = forms.IntegerField(label='Choix du de la catégorie',
                                           widget=forms.Select(choices=categories_tuples))

    # Liste déroulante courses (liste ne peut-être que sous forme de tuples)
    courses = Course.objects.using('default')
    courses_name_list = []
    courses_id_list = []
    for course in courses:
        courses_id_list.append(course.id)
        courses_name_list.append(course.name)
    courses_tuples = list(zip(courses_id_list, courses_name_list))
    # Renvoi de l'id
    courses_choice = forms.IntegerField(label='Choix de la course', widget=forms.Select(choices=courses_tuples))

    pax = forms.IntegerField(label='Nombre de personnes')
    time = forms.IntegerField(label='Temps de préparation')
    instructions = forms.CharField(label='Nom', max_length=100)
    cat = Category.objects.using('default')

    # Liste déroulante ingrédients (liste ne peut-être que sous forme de tuples)
    ingredients = Ingredient.objects.using('default')
    ingredients_name_list = []
    ingredients_id_list = []
    for ingredient in ingredients:
        ingredients_id_list.append(ingredient.id)
        ingredients_name_list.append(ingredient.name)
    ingredients_tuples = list(zip(ingredients_id_list, ingredients_name_list))
    # Renvoi de l'id
    ingredients_choice = forms.IntegerField(label='Choix du de la catégorie',
                                            widget=forms.Select(choices=ingredients_tuples))

    # Liste déroulante unités (liste ne peut-être que sous forme de tuples)
    units = MeasurementUnit.objects.using('default')
    units_name_list = []
    units_id_list = []
    for unit in units:
        units_id_list.append(unit.id)
        units_name_list.append(unit.name)
    units_tuples = list(zip(units_id_list, units_name_list))
    # Renvoi de l'id
    units_choice = forms.IntegerField(label='unité',
                                      widget=forms.Select(choices=units_tuples))

    quantity = forms.IntegerField(label='Quantité')


RecepeFormset = formset_factory(AddRecipeForm, extra=1)


# TO BE ADDED
# category = forms.ModelChoiceField(queryset=Recipe.category_id.all(), empty_label="(Nothing)")
# image = forms.ImageField()

# endregion recipes


# region units
class UpdateUnitForm(forms.Form):
    id = forms.IntegerField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    name = forms.CharField(label='Nom', max_length=100)


class AddUnitForm(forms.Form):
    name = forms.CharField(label='Nom', max_length=100)


# endregion units


# region ingredients
class UpdateIngredientForm(forms.Form):
    id = forms.IntegerField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    name = forms.CharField(label='Nom', max_length=100)


class AddIngredientForm(forms.Form):
    name = forms.CharField(label='Nom', max_length=100)


# endregion ingredients


# region courses
class AddCourseForm(forms.Form):
    name = forms.CharField(label='Nom', max_length=100)


class UpdateCourseForm(forms.Form):
    id = forms.IntegerField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    name = forms.CharField(label='Nom', max_length=100)


# endregion courses

# region categories
class AddCategoryForm(forms.Form):
    name = forms.CharField(label='Nom', max_length=100)


class UpdateCategoryForm(forms.Form):
    id = forms.IntegerField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    name = forms.CharField(label='Nom', max_length=100)

# endregion categories
