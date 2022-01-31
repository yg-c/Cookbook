from django import forms
from .models import *


# region recipes

class AddRecipeForm(forms.Form):
    name = forms.CharField(label='Nom', max_length=100)


class SortRecipesByCourse(forms.Form):
    # Création de la liste déroulante des plats (une liste ne peut-être que sous forme de tuples)
    courses = Course.objects.all()
    course_name_list = []
    course_id_list = []

    for c in courses:
        course_id_list.append(c.id)
        course_name_list.append(c.name)

    course_tuple = list(zip(course_id_list, course_name_list))
    
    # Renvoi de l'id
    course_choice = forms.IntegerField(label='Choix du plat', widget=forms.Select(choices=course_tuple))

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
