from django.urls import path
from cookbook import views


urlpatterns = [
    path('', views.index, name='index'),
    path('units/', views.measurmentunits, name='units'),
    path('unit/<int:pk>', views.measurmentunit, name='unit'),
    path('recipes/', views.getallrecipes, name='recipes'),
    path('recipe/<int:pk>', views.detailselectedrecipe, name='recipe'),
    path('updateunit/<int:pk>', views.updateunit, name='updateunit'),
]
