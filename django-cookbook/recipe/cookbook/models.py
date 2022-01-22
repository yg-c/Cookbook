from django.db import models


# Recipe DB
class MeasurementUnit(models.Model):
    id = models.BigAutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=200, db_column='name')

    objects = models.Manager()

    class Meta:
        db_table = "measurement_unit"

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.BigAutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=200, db_column='name')

    objects = models.Manager()

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.BigAutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=200, db_column='name')

    objects = models.Manager()

    class Meta:
        db_table = "course"

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    id = models.BigAutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=200, db_column='name')

    objects = models.Manager()

    class Meta:
        db_table = "ingredient"

    def __str__(self):
        return self.name


class Recipe(models.Model):
    id = models.BigAutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=200, db_column='name')
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT, db_column='category_id')
    course_id = models.ForeignKey(Course, on_delete=models.PROTECT, db_column='course_id')
    pax = models.PositiveIntegerField(db_column='pax')
    preparation_time = models.PositiveIntegerField(db_column='preparation_time')
    instructions = models.TextField(db_column='instructions')

    objects = models.Manager()

    class Meta:
        db_table = "recipe"

    def __str__(self):
        return self.name


class IngredientRecipe(models.Model):
    id = models.BigAutoField(primary_key=True, db_column='id')
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, db_column='recipe_id')
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.PROTECT, db_column='ingredient_id')
    quantity = models.DecimalField(decimal_places=2, max_digits=15, db_column='quantity')
    measurement_unit_id = models.ForeignKey(MeasurementUnit, on_delete=models.PROTECT, db_column='measurement_unit_id')

    objects = models.Manager()

    class Meta:
        db_table = "ingredient_recipe"

    def __str__(self):
        str_id = str(self.id)
        return str_id
