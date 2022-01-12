from django.urls import path
from cookbook import views

urlpatterns = [
    path('', views.index, name='index'),
    path('units/', views.measurementunits, name='units'),
    path('unit/<int:pk>', views.measurementunit, name='unit'),
    path('recipes/', views.getallrecipes, name='recipes'),
    path('recipe/<int:pk>', views.detailselectedrecipe, name='recipe'),
    path('updateunit/<int:pk>', views.updateunit, name='updateunit'),
    path('addunit/', views.addunit, name='addunit'),
    path('deleteunit/<int:pk>', views.deleteunit, name='deleteunit'),
    path('ingredients/', views.getallingredients, name='ingredients'),
    path('addingredient/', views.addingredient, name='addingredient'),
    path('deleteingredient/<int:pk>', views.deleteingredient, name='deleteingredient'),
    path('courses/', views.getallcourses, name='courses'),
    path('addcourse/', views.addcourse, name='addcourse'),
    path('updatecourse/<int:pk>', views.updatecourse, name='updatecourse'),
    path('deletecourse/<int:pk>', views.deletecourse, name='deletecourse')
]
