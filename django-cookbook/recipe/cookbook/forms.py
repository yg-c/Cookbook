from django import forms
from .models import *


# region recipes

class AddRecipeForm(forms.Form):
    name = forms.CharField(label='Nom', max_length=100)

    # Liste déroulante courses (liste ne peut-être que sous forme de tuples)
    courses = Course.objects.using('default')
    courses_name_list = []
    courses_id_list = []
    for course in courses:
        courses_id_list.append(course.id)
        courses_name_list.append(course.name)
    courses_tuples = list(zip(courses_id_list, courses_name_list))
    # Renvoi de l'id
    courses_choice = forms.IntegerField(label='Choix du restaurant', widget=forms.Select(choices=courses_tuples))

# TO BE ADDED
# image = forms.ImageField()
#    nbpeople = forms.IntegerField
    #category = forms.ModelChoiceField(queryset=Recipe.category_id.all(), empty_label="(Nothing)")


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
