from django import forms
from .models import *

# region recipes

class AddRecipeForm(forms.Form):
    name = forms.CharField(label='Nom', max_length=100)
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
